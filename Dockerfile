FROM python:3.10

RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    apt-get clean

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install TTS

CMD ["python", "app.py"]
