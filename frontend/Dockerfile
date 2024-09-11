FROM registry.fedoraproject.org/f33/python3

WORKDIR /app

RUN yum update -y && yum install -y \
    gcc \
    gcc-c++ \
    curl \
    yum-utils \
    git \
    && yum clean all


EXPOSE 8501

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

COPY app.py .

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

