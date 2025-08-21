
# Clean setup for testing database interactions in isolation

### Summary
The project uses `Docker` to containerize a lightweight `Python` app that writes timestamped messages into a local `SQLite` database. The `docker-compose.yaml` orchestrates the build and runtime environment, while mounting ensures the database file persists outside the container.

### File structure
```bash
06_sqlite_and_docker/
├── app/
│   ├── data.db
│   └── main.py
├── docker-compose.yml
└── Dockerfile
```

### Dependencies/imports
The scripts use the following Python modules:
```
datetime
sqlite3
```

### Setup & commands
To run the project for the first time:
```bash
# cd 06_sqlite_and_docker/
docker compose up --build
```

Subsequent container runs can be triggered using:
```bash
# cd 06_sqlite_and_docker/
docker compose start
```

If you would like to interact with the database in the terminal, we get the `sqlite-app` argument from the `docker-compose.yml` under `services:` and run the following command:

```bash
# cd 06_sqlite_and_docker/
docker compose run --service-ports sqlite-app bash
```

The interactive terminal inside the container will takeover your current terminal tab. First we install sqlite3 so we can interact with the db.
```bash
root@containerID:/app# apt update
root@containerID:/app# apt install sqlite3
root@containerID:/app# sqlite3 data.db
```

You can now interact with the databases inside `data.db`
```bash
sqlite> .help
sqlite> .databases
main: /app/data.db r/w

sqlite> .tables
messages

sqlite> SELECt * FROM messages
   ...> ;
1|Hello from Docker at 2025-08-18T19:42:07|2025-08-18T19:42:07
2|Hello from Docker at 2025-08-18T19:43:05|2025-08-18T19:43:05
3|Hello from Docker at 2025-08-21T02:36:07|2025-08-21T02:36:07
4|Hello from Docker at 2025-08-21T02:42:05|2025-08-21T02:42:05
sqlite>

sqlite> .exit
root@containerID:/app# exit
```

If you want the container to stay alive after the script finishes (so you can exec into it later), you can tweak your `docker-compose.yml` like this:
```yml
command: tail -f /dev/null
```
