### Запуск 

```bash
just up users
```
> Обратите внимание, что приложению требуются DATABASE_URL, REDIS_URL и KAFKA_URL

### Миграции

#### Применить миграции

```bash
alembic upgrade head
```

#### Создать миграцию 

```bash
alembic revision --autogenerate -m "{action}"
```
