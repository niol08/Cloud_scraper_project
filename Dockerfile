# Dockerfile
FROM mcr.microsoft.com/playwright/python:latest


WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "scheduler.py"]
