FROM python:3.11-slim

WORKDIR /app

COPY app/main.py .

# Optional, sqlite3 is part of Python's standard library
# RUN pip install --no-cache-dir sqlite3

CMD ["python", "main.py"]