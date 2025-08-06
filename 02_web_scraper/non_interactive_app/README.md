# Containerize a Python web scraper app
The Python script uses `requests` & `beautifulsoup4`
```
beautifulsoup4==4.13.4
requests==2.32.4
```

The Dockerfile has been configured to install the requirements
```docker
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
```

### Expected output when the Docker Container is run
Each time you run the container, a different (randomly selected movie) should appear in the terminal.
```
3. The Dark Knight (2008), Rating: 9.1
```

### Create the Docker Image & run the Docker Container

```bash
cd non_interactive_app/
docker build -t python-imdb-scraper-t . 
docker run --rm python-imdb-scraper-t
```

---
