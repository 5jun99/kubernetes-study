# service_b.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    # Service C 호출
    try:
        r = requests.get("http://c-service:8080/")
        return f"Hello from Service B! C says: {r.text}\n"
    except:
        return "Hello from Service B! C unreachable\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
