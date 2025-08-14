from flask import Flask, request
import threading, time, requests

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json
    print(f"[App B] Received: {data['text']}")
    return {"response": f"App B got your message: {data['text']}"}, 200


def send_to_a():
    while True:
        time.sleep(10)
        try:
            response = requests.post("http://app_a:5000/message", json={"text": "Hello from B"})
            print("[App B] Response from A:", response.json()["response"])
        except Exception as e:
            print("[App B] Error sending to A:", e)


if __name__ == '__main__':
    threading.Thread(target=send_to_a, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
