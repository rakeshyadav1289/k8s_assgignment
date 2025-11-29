from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    backend_url = "http://backend-service:5000/data"
    data = requests.get(backend_url).json()
    return f"<h1>Flask Frontend</h1><p>Backend says: {data}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
