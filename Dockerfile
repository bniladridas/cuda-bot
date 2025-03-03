FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install python-dotenv

COPY . .

CMD ["python3", "bot.py"]
