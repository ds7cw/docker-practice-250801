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
Each time you run the container, a different (randomly selected movie) should appear in the terminal. Type 'y', to generate a new movie title.
```
11. Forrest Gump (1994), Rating: 8.8
Would you like to select another movie (y/[n])?
```

### Create the Docker Image & run the Docker Container
We're using the `-it` flags to enable an interactive pseudo terminal.
```bash
cd interactive_app/
docker build -t python-imdb-scraper-it . 
docker run --rm -it python-imdb-scraper-it
```

---
