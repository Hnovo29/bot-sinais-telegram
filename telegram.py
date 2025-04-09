import requests

TELEGRAM_TOKEN = '7785668664:AAGsUfDE35zeVx54SUBvG6sSL8sJwF2EWWM'
TELEGRAM_CHAT_ID = '-1002673363905'

def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": mensagem, "parse_mode": "HTML"}
    requests.post(url, data=data)
