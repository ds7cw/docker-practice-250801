import socket
import random
import time
import threading

phrases = [
    "Hello from client!",
    "Client says hi!",
    "Ping from client!",
    "Client is alive!",
    "What's up from client?"
]

def handle_server(conn, addr):
    print(f"Client: Connected to {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Client: Received from server: {data}")
        except:
            break
    conn.close()
    print(f"Client: Connection closed with {addr}")


def send_messages():
    while True:
        time.sleep(10)
        try:
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.connect(('server', 9999))
            message = random.choice(phrases)
            server_sock.send(message.encode())
            print(f"Client: Sent to server: {message}")
            server_sock.close()
        except Exception as e:
            print(f"Client: Error sending message: {e}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Client: Listening on port 9999")

    threading.Thread(target=send_messages, daemon=True).start()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_server, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
