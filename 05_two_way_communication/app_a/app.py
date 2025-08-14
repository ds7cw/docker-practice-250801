from flask import Flask, request
import threading, time, requests

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json
    print(f"[App A] Received: {data['text']}")
    return {"response": f"App A got your message: {data['text']}"}, 200


def send_to_b():
    while True:
        time.sleep(10)
        try:
            response = requests.post("http://app_b:5000/message", json={"text": "Hello from A"})
            print("[App A] Response from B:", response.json()["response"])
        except Exception as e:
            print("[App A] Error sending to B:", e)


if __name__ == '__main__':
    threading.Thread(target=send_to_b, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
