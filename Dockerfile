FROM python as poetry-requirements-export
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt


FROM python:3.10
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY --from=poetry-requirements-export /app/requirements.txt .
RUN pip install -r requirements.txt
COPY money ./money
CMD python ./money/manage.py runserver 0.0.0.0:8000
