# Set up a two-way container interaction using Docker Compose

### Summary
- To run this setup, save all files in the same directory and execute `docker-compose up --build`.
- The containers will communicate over a private bridge network (`app-network`).
- Each container runs a Python script that acts as both a server (listening on port 9999) and a client (sending messages to the other container).
- Messages are randomly selected from a predefined list and sent every 10 seconds.
- You'll see the sent and received messages in
the terminal output of each container, prefixed with "Server:" or "Client:".
- The `PYTHONUNBUFFERED=1` environment variable ensures real-time logging.
- No ports are exposed externally, keeping the communication secure within the Docker network.

### File structure
```bash
05_two_way_communication/
├── client/
│   ├── client.py
│   └── Dockerfile
├── server/
│   ├── server.py
│   └── Dockerfile
├── docker-compose.yml
```

### Dependencies/imports
The scripts use the following Python modules:
```
socket
random
time
threading
```

### Project description
Two Python apps have been created — a server and a client — each running in its own Docker container. Both apps:
- Listen on TCP port `9999`
- Periodically send messages to each other
- Accept incoming connections and print received messages

They communicate over a Docker bridge network (`app-network`), which isolates traffic from the outside world — so this is a secure, internal-only setup.

### TCP Socket Communication

Both apps use Python’s `socket` module to create TCP sockets (`SOCK_STREAM`), which are reliable, connection-oriented channels.

- `bind()`: Assigns the socket to a local IP and port.
- `listen()`: Starts listening for incoming connections.
- `accept()`: Waits for a client to connect, then returns a new socket (`conn`) and the client’s address.
- `connect()`: Initiates a connection to a remote socket.
- `send()` / `recv()`: Transmit and receive data over the connection.

### Threading

Each app uses `threading.Thread` to:
- Run a background loop that sends messages every 10 seconds.
- Handle each incoming connection in a separate thread, allowing multiple clients to be served concurrently.

### Understanding `conn.recv(1024).decode()`
```python
data = conn.recv(1024).decode()
```

`conn.recv(1024)`:
- Reads up to 1024 bytes from the socket.
- This is a buffer size — not a limit on total message size, just how much to read in one go.
- If the message is longer than 1024 bytes, you'd need to call `recv()` again to get the rest.

1024 is a common default — large enough for simple messages, small enough to avoid memory waste. You can adjust it based on expected message size (e.g. 4096 for larger payloads).

`.decode()`:
- Converts the raw bytes received into a human-readable string.
- TCP transmits data as bytes, so decoding (usually with `UTF-8`) is necessary to interpret it as text.

### Message flow

- Client starts and listens on port 9999.
- Server starts and listens on port 9999.
- Every 10 seconds:
    - Server connects to client and sends a random message.
    - Client connects to server and sends a random message.
- Each app accepts incoming connections and prints the received message.

This creates a bidirectional ping-pong of messages over TCP.

### Docker Compose & networking

The `docker-compose.yml` sets up:
- Two services (`server` and `client`)
- A shared bridge network (`app-network`)
- Internal DNS resolution: `client` can reach `server` via hostname `server`, and vice versa

No ports are exposed to the host machine.

### Expected output when the Docker Containers are up & running
Build the images before starting the containers
```bash
cd 05_two_way_communication
docker compose up --build
```

```bash
...
[+] Running 4/4
 ✔ 05_two_way_communication-server
 ✔ 05_two_way_communication-client
 ✔ Container server
 ✔ Container client
Attaching to client, server
server  | Server: Listening on port 9999
client  | Client: Listening on port 9999
server  | Server: Sent to client: Ping from server!
client  | Client: Connected to ('000.00.0.2', 12345)
client  | Client: Received from server: Ping from server!
client  | Client: Connection closed with ('000.00.0.2', 12345)
client  | Client: Sent to server: Hello from client!
server  | Server: Connected to ('000.00.0.3', 54321)
server  | Server: Received from client: Hello from client!
server  | Server: Connection closed with ('000.00.0.3', 54321)
server  | Server: Sent to client: What's up from server?
```
