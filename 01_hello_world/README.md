# Create a Docker Image from a simple Python script

### Expected output when the Docker Container is run (time & date will vary)
```
Hello World!
Current time & date: 2025-08-01 08:00:00
```

### Create the Docker Image & run the Docker Container
```bash
cd 01_hello_world/
docker build -t hello-world-python-app .
docker run --rm hello-world-python-app
```

### Helper commands
```bash
docker images
docker ps -a
docker rm "container_id"
docker rmi "image_id"
```

---
