# Сервис рекомендаций товаров 

## Сборка 

```bash
docker build -t rust-svc --build-arg BIN=recommendations .
docker run --rm -p 8080:8080 rust-svc 
```
