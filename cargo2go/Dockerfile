FROM python:3.11-slim

WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt ./

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8000
ENV PORT=8080

# Define environment variable
