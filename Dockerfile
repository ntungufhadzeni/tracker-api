# base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# set working directory
WORKDIR /app

# copy Pipfile & unlock (to avoid dependency errors)
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./app .


CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]