set shell := ["bash", "-euo", "pipefail", "-c"]

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

up:
    sudo docker compose up --build

down:
    sudo docker compose down
