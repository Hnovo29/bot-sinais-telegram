from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from telegram import enviar_mensagem
from analisador import analisar_padrao

def iniciar_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

def extrair_resultados(driver):
    driver.get("https://leon111.bet/live-casino/evolution-games/play/bac-bo")
    time.sleep(10)  # tempo para a página carregar completamente
    resultados = driver.find_elements(By.CLASS_NAME, 'history-item')
    historico = []
    for item in resultados[:15]:
        texto = item.text.lower()
        if 'red' in texto:
            historico.append('🔴')
        elif 'blue' in texto:
            historico.append('🔵')
        elif 'tie' in texto:
            historico.append('🟠')
    return historico[::-1]  # do mais antigo ao mais recente

def main():
    driver = iniciar_driver()
    ultimo_sinal = ''

    while True:
        try:
            historico = extrair_resultados(driver)
            if len(historico) < 5:
                continue
            sinal = analisar_padrao(historico)
            if sinal and sinal != ultimo_sinal:
                mensagem = f"<b>ENTRADA CONFIRMADA</b> 🎰\n🎲 Apostar na cor {sinal}\n🎲 Proteger o empate 🟠\n📊 Fazer até 2 gales"
                enviar_mensagem(mensagem)
                ultimo_sinal = sinal
            time.sleep(15)
        except Exception as e:
            print("Erro:", e)
            time.sleep(10)

if __name__ == '__main__':
    main()
