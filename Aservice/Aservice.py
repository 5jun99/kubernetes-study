# service_a.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    # Service B 호출
    try:
        r = requests.get("http://b-service:8080/")
        return f"Hello from Service A! B says: {r.text}\n"
    except:
        return "Hello from Service A! B unreachable\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
