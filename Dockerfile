# Dockerfile
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy



WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "scheduler.py"]
