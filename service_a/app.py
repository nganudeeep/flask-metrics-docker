from flask import Flask
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def index():
    res = requests.get("http://service_b:5001/hello")
    return f"Service A calling -> {res.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
