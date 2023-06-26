# Base image
FROM tiangolo/uvicorn-gunicorn:python3.11-slim

RUN apt-get update && apt-get install -y netcat

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the application code
COPY api .

