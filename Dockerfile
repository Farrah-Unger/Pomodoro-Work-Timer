FROM python:3.11
RUN apt-get update && apt-get install -y xvfb
ENV DISPLAY :1
COPY pomodoro-start /app
WORKDIR /app
CMD python main.py