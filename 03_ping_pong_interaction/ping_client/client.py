import requests

def main():
    response = requests.get("http://pong:5000/ping")
    print("Response from pong:", response.text)

if __name__ == "__main__":
    main()
