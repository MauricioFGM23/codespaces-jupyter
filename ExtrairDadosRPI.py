from unidecode import unidecode  # Certifique-se de ter o pacote 'unidecode' instalado
import pandas as pd
import os

# Obtenção dos dados pelos arquivos
def dados_arquivos(caminho_arquivo):
    # Abrir o arquivo txt
    with open(caminho_arquivo, "r", encoding="latin-1") as arquivo:
        # Ler todas as linhas do arquivo
        print(f"Conteúdo do arquivo '{caminho_arquivo}': \n")
        linhas = arquivo.readlines()

    # Variável para indicar se estamos dentro de um bloco de texto com "(21)"
    dentro_do_bloco = False

    # Variável para armazenar o texto do bloco atual
    texto_bloco = ""
    
    # Lista para armazenar todos os blocos encontrados
    lista_blocos = []

    # Percorrer todas as linhas do arquivo
    for linha in linhas:
        if linha.startswith("(21)") or linha.startswith("(11)"):
            # Se encontrarmos um novo bloco, verificamos se o texto anterior possui "UNIVERSIDADE DE BRASILIA"
            if dentro_do_bloco and "UNIVERSIDADE DE BRAS" in unidecode(texto_bloco).upper():
                # Adicionamos o texto do bloco à lista de blocos
                lista_blocos.append(texto_bloco.split("\n"))
                
            # Reiniciamos o texto do bloco e marcamos que estamos dentro de um novo bloco
            dentro_do_bloco = True
            texto_bloco = linha
            
        else:
            # Se estivermos dentro de um bloco, continuamos a acumular o texto
            if dentro_do_bloco:
                texto_bloco += linha
            
    # Verificamos o último bloco após sair do loop
    if dentro_do_bloco and "UNIVERSIDADE DE BRAS" in unidecode(texto_bloco).upper():
        # Adicionamos o último bloco à lista de blocos
        lista_blocos.append(texto_bloco)
        
    return lista_blocos

# Preenchimento dos dados na planilha:
def extrair_bloco(planilha, entrada_dados):
    data_dict = {}
    for line in entrada_dados:
        if line.startswith("(21)"):
            data_dict["(21) numero do pedido"] = line[5:].strip()
        elif line.startswith("(22)"):
            data_dict["(22) data do deposito"] = line[5:].strip()
        elif line.startswith("(71)"):
            data_dict["(71) titulares"] = line[5:].strip()
        elif line.startswith("(72)"):
            data_dict["(72) autores"] = line[5:].strip()
        elif line.startswith("(54)"):
            data_dict["(54) titulo"] = line[5:].strip()
        elif line.startswith("(co)"):
            data_dict["(co) comentario"] = line[5:].strip()
        elif line.startswith("(Cd)"):
            data_dict["(Cd) código da exigencia"] = line[5:].strip()
        elif line.startswith("(11)"):
            data_dict["(11) numero da patente"] = line[5:].strip()
        elif line.startswith("(RPI) "):
            data_dict["(RPI) numero da revista"] = line[5:].strip()

    try:
        # Load the existing data from the "dadosRPI.csv" file
        df = pd.read_excel(planilha)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with the extracted data
        df = pd.DataFrame([data_dict])
    else:
        # Append the data from the current block to the existing DataFrame
        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)

    df.to_excel(planilha, index=False)

if __name__ == "__main__":
    pasta = "/workspaces/codespaces-jupyter/RPISpider/downloads"
    arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.txt')]
    planilha = "/workspaces/codespaces-jupyter/RPISpider/resultados/Dados RPI.xlsx"

    # Aplica a função em cada arquivo .txt encontrado.
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        print(f"Lendo o arquivo: {arquivo}")
        lista_blocos = dados_arquivos(caminho_arquivo)  # Armazena todos os blocos em uma lista
        lista_blocos.insert(0,["(RPI) " + arquivo])
        print(lista_blocos)
        for dados in lista_blocos:
            extrair_bloco(planilha, dados)
        print("Os dados foram gravados em 'Resultados.txt'.\n")
