from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Adicione o caminho do chromedriver ao PATH
os.environ["PATH"] += os.pathsep + "/usr/lib/chromium-browser/"

# Crie uma instância do ChromeDriver com a opção headless, sem precisar iniciar o navegador
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
# criar configurações que permitem o download sem confirmação
chrome_options.add_argument("--disable-notifications") # Desativar as notificações
chrome_options.add_argument("--incognito") # Executar em modo privado
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": '/workspaces/codespaces-jupyter/RPISpider/downloads', # Definir o diretório de download
  "download.prompt_for_download": False, # Não pedir confirmação para baixar
  "download.directory_upgrade": True,
  "safebrowsing_for_trusted_sources_enabled": False,
  "safebrowsing.enabled": False
})

# Navegue até a página do INPI/RPI
driver.get("http://revistas.inpi.gov.br/rpi/")

#intervalos de datas
datainit = '01122022'
datafim = '01012023'

# Seleciona os campos "Buscar Patentes"
selecao = driver.find_element(By.XPATH, '//a[@class="showTipoRevistaBusca"][@id="6"]')
selecao.click()
time.sleep(1)

selecao0 = driver.find_element(By.XPATH, '//input[@class="showTipoPesquisaData"][@value="2"]')
selecao0.click()
time.sleep(1)

selecao1 = driver.find_element(By.XPATH, '//input[@name="revista.dataInicialp"]')
selecao1.click()
selecao1.send_keys(datainit)
time.sleep(1)

selecao2 = driver.find_element(By.XPATH, '//input[@name="revista.dataFinalp"]' )
selecao2.click()
selecao2.send_keys(datafim)
time.sleep(1)

selecao3=driver.find_element(By.XPATH, '//form[@id="buscaPorData"]//button[@type="submit"]')
selecao3.click()
time.sleep(1)

#extrair o texto da página
#textoall = driver.find_elements(By.XPATH, "//*[text()]")
#for texto in textoall:
#    print(texto.text)

#Realizar download dos arquivos
links = driver.find_elements(By.XPATH, '//table[@id="result"]//a[contains(text(), "TXT")]')
for e in links:
    print(e.get_attribute('href'))
    e.click()
    time.sleep(3)

print("Download das RPI concluido!")

driver.quit()
