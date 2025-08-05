FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

# docker build -t python-imdb-scraper-it . 
# docker run --rm -it python-imdb-scraper-it