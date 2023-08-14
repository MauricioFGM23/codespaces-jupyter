from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import zipfile
import time
import os

#intervalos de datas e diretório de download
datainit = input("Data Inicial: ")
datafim = input("Data Final:  ")
#diretorio = input("Diretório para Download: ")
print("Iniciando download das RPI!!!\n")
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
  "download.default_directory": '/workspaces/codespaces-jupyter/RPISpider/downloads/', # Definir o diretório de download
  "download.prompt_for_download": False, # Não pedir confirmação para baixar
  "download.directory_upgrade": True,
  "safebrowsing_for_trusted_sources_enabled": False,
  "safebrowsing.enabled": False
})

# Navegue até a página do INPI/RPI
driver.get("http://revistas.inpi.gov.br/rpi/")

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

#Realizar download dos arquivos
links = driver.find_elements(By.XPATH, '//table[@id="result"]//a[contains(text(), "TXT")]')
for e in links:
    print(e.get_attribute('href'))
    e.click()
    time.sleep(2)

print("Download das RPI concluido! Iniciando descompressão.")

driver.quit()

def extract_all_zips_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(folder_path, file_name)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
            print(f"Extraiu {file_name}")
            time.sleep(1)

def excluir_arquivos_xml(diretorio):
    try:
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".xml"):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                os.remove(caminho_arquivo)
        print("Arquivos indesejados excluídos!!!\n")
               

    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    diretorio_alvo = "/workspaces/codespaces-jupyter/RPISpider/downloads/"
    extract_all_zips_in_folder(diretorio_alvo)
    excluir_arquivos_xml(diretorio_alvo)
    print("Descompressão completa!!! Fechando programa.\n")


exit()
