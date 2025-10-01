# Dockerfile - runtime image for calculator app
FROM python:3.11-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY calculator.py main.py ./

# run the interactive menu
CMD ["python", "main.py"]
