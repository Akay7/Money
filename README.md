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

## FAQ (or better say IAQ - infrequently asked questions)

1. Q: Is it possible to use same TCP port in multiple instances of application? 

    A: Yes, since [SO_REUSEPOR](https://lwn.net/Articles/542629/) is already implemented at latest kernels of Linux. Then it's possible to start multiple servers that will listen at the same address:port. But in that case this app will required something more robust than a django dev server. For example it's possible achieve with [--reuse-port](https://docs.gunicorn.org/en/stable/settings.html?highlight=reuse-port#reuse-port) flag of gunicorn. So it's possible to achieve with multiple calls of the next command on linux systems:
```gunicorn money.wsgi:application --bind 0.0.0.0:8000 --reuse-port```. On windows systems it's probably possible too but it's not so well documented and possibly it's gonna take more trials.
2. Q: Is it possible that multiple docker containers will listen on the same address:port?

   A: Yes, it's possible but we should expose port from the different containers with different protocols(TCP, UDP).
3. Q: Which design patters is useful with Django?

    A: A tricky one. Since patters seems more from Java or .Net world then from dynamic world of python. But there's a book [Django Design Patterns and Best Practices - Second Edition by Arun Ravindran it describes](https://www.packtpub.com/product/django-design-patterns-and-best-practices-second-edition/9781788831345) where described some patterns in context of Development with python-Django. 
