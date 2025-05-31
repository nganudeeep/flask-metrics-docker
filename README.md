# 📊 flask-metrics-docker

A lightweight observability project featuring two Flask microservices deployed with Docker, monitored using Prometheus and visualized in Grafana.

## 🧱 Architecture

- `service_a`: Calls `service_b` and exposes Prometheus metrics.
- `service_b`: Responds with a message and exposes Prometheus metrics.
- Prometheus: Scrapes metrics from both Flask services.
- Grafana: Visualizes request count, latency, and more.

All containers are connected via a custom Docker bridge network.
