import requests

# Coloque seus dados diretamente aqui
TOKEN = "7785668664:AAGsUfDE35zeVx54SUBvG6sSL8sJwF2EWWM"
CHAT_ID = "-1002673363905"

# Mensagem de exemplo
mensagem = "Bot de sinais iniciado com sucesso!"

# Envia a mensagem para o canal
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print("Erro ao enviar mensagem:", response.text)
