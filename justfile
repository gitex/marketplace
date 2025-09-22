#!/usr/bin/env just --justfile

set shell := ["bash", "-euo", "pipefail", "-c"]
set dotenv-load := true
set export := true

default:
    @just --list

ENV_DIR := "./infra/env"

create-default-env reset="false":
    #!/usr/bin/env sh
    shopt -s nullglob
    mkdir -p {{ ENV_DIR }}
    status=0
    for src in {{ ENV_DIR }}/example.*; do
      name="${src##*/}"            # example.NAME
      base="${name#example.}"      # NAME
      dst="{{ ENV_DIR }}/.${base}"   # .NAME
      if [ -e "$dst" ]; then
        if cmp -s "$src" "$dst"; then
          echo "skip (exists, same): $dst"
        else
          if [ "{{ reset }}" = "true"]; then 
              install -D -m 0644 "$src" "$dst"
              echo "reset: $dst"
          else 
              echo "skip (exists, different!): $dst (use just create-default-env reset=true)" >&2
              status=1
          fi
       fi
        continue
      fi
      install -D -m 0644 "$src" "$dst"
      echo "created: $dst"
    done
    exit $status

reset-volumes:
    docker compose down --volumes

PYPI_PROFILE := "pypi"

up target="users":
    sudo docker compose --profile {{ PYPI_PROFILE }} up -d
    sudo docker compose --profile {{ target }} up 

down target="users":
    sudo docker compose --profile {{ PYPI_PROFILE }} down --remove-orphans
    sudo docker compose --profile {{ target }} down --remove-orphans

ps:
    sudo docker compose ps --all

logs target:
    sudo docker logs -f {{ target }} 

status:
    sudo docker compose ps --all --format '{{ "{{" }}.State{{ "}}" }} {{ "{{" }}.Service{{ "}}" }}' | \
    while read -r state service; do \
      if [[ "$state" == "running" ]]; then icon="✅"; else icon="❌"; fi; \
      printf "%s \033[36m%s\033[0m\n" "$icon" "$service"; \
    done

alias st := status
