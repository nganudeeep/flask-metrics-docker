FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask prometheus_flask_exporter
CMD ["python", "app.py"]
