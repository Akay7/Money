# MONEY

## Information

API locates at `api/v1/`

## Run application

```bash
docker-compose up --build
docker compose run --rm backend /bin/bash -c  "python3 money/manage.py migrate"
```

navigate to `http://127.0.0.1:8000/api/v1/` at browser

### Shutdown

```bash
docker-compose down -v
```

## Development

Install pre-commit

```bash
pre-commit install
```
