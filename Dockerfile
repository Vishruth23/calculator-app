# Dockerfile - runtime image for calculator app
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py main.py ./

CMD ["python", "main.py"]
