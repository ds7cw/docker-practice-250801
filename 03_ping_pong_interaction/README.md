# Set up container interaction using Docker Compose

### File structure
```bash
03_ping_pong_interaction/
├── pong_app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── ping_client/
│   ├── client.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
```

### Dependencies
The Python scripts use `requests` & `Flask`
```dos
Flask==3.1.1
requests==2.32.4
```

### Expected output when the Docker Containers are up & running
Build the images before starting the containers
```bash
cd 03_ping_pong_interaction
docker compose up --build 
```

```bash
 ...
 ✔ Network 03_ping_pong_interaction_internal  Created 0.1s 
 ✔ Container 03_ping_pong_interaction-pong-1  Created 0.0s 
 ✔ Container 03_ping_pong_interaction-ping-1  Created 0.0s 
Attaching to ping-1, pong-1
pong-1  |  * Serving Flask app 'app'
pong-1  | Press CTRL+C to quit
ping-1  | Response from pong: pong
ping-1 exited with code 0
```

---
