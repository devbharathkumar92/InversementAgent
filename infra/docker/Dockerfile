# AI Investment Opportunity Agent — API/worker image (bootstrap scaffold).
# Application services are implemented by their topics; this is the base image only.
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --upgrade pip && pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["uvicorn", "src.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"]