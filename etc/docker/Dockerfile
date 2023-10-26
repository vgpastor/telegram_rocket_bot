FROM python:3.10

WORKDIR /app/main

RUN true && apt update && apt install -y curl gnupg2 jq
# RUN true &&  curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc |  tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" |  tee /etc/apt/sources.list.d/ngrok.list &&  apt update &&  apt install ngrok
#
# COPY ./etc/docker/start.sh /app/start.sh
# RUN chmod +x /app/start.sh

COPY . /app/main

RUN pip install -r requirements.txt

CMD ["python3","/app/main/main.py"]
