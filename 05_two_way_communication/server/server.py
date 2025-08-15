import socket
import random
import time
import threading

phrases = [
    "Hello from server!",
    "Server says hi!",
    "Ping from server!",
    "Server is alive!",
    "What's up from server?"
]

def handle_client(conn, addr):
    print(f"Server: Connected to {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Server: Received from client: {data}")
        except:
            break
    conn.close()
    print(f"Server: Connection closed with {addr}")

def send_messages():
    while True:
        time.sleep(10)
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect(('client', 9999))
            message = random.choice(phrases)
            client_sock.send(message.encode())
            print(f"Server: Sent to client: {message}")
            client_sock.close()
        except Exception as e:
            print(f"Server: Error sending message: {e}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server: Listening on port 9999")

    threading.Thread(target=send_messages, daemon=True).start()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
