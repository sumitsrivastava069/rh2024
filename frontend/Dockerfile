FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8501

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

COPY app.py .

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

