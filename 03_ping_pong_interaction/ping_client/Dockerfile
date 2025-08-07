FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY client.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "client.py"]
