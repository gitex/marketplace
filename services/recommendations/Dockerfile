ARG RUST_VERSION=1.80 
FROM rust:${RUST_VERSION}-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends pkg-config libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Cargo.toml Cargo.lock ./ 

RUN cargo fetch 

COPY . . 
ARG BIN=app 
RUN cargo build --release --bin ${BIN}

# Runtime 
FROM debian:bookworm-slim as runtime 

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
WORKDIR /app 

ARG BIN=app 

COPY --from=builder /app/target/release/${BIN} /usr/local/bin/${BIN}

USER appuser 
EXPOSE 8080 
ENTRYPOINT ["/usr/local/bin/app"]

