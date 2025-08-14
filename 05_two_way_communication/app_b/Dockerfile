FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip3 install --no-cache-dir flask requests

CMD ["python", "app.py"]