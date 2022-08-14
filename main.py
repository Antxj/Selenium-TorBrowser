# Obs: o navegador Tor precisa estar aberto.
# https://www.torproject.org/download/

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Chrome e Proxy Tor
servico = Service(ChromeDriverManager().install())
proxy = "socks5://127.0.0.1:9150"  # Tor
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy}")
navegador = webdriver.Chrome(service=servico, options=chrome_options)

check_tor = 'https://check.torproject.org/'
navegador.get(check_tor)

time.sleep(20)
navegador.quit()
