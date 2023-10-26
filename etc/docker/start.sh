#!/bin/bash

set -a
source ./env
set +a

ngrok http 8666 & sleep 10 && export BERNARD_BASE_URL=$(curl --silent http://127.0.0.1:4040/api/tunnels | jq -r '.tunnels[0].public_url')

#https://api.telegram.org/bot6085702257:AAHfRfXtn4Vaf6sKAm3g02c_vlTRBl7Mvo8/setWebhook?url=https://bae3-79-116-188-183.ngrok.io/hooks/telegram/8e123b5bb45354780b97d956dd828e0aa353d24d83bc1de8bb9bf14b37fc47d5
#https://api.telegram.org/bot6085702257:AAHfRfXtn4Vaf6sKAm3g02c_vlTRBl7Mvo8/getWebhookInfo
python start.py run
