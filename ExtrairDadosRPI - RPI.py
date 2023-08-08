from unidecode import unidecode  # Certifique-se de ter o pacote 'unidecode' instalado
from SalvarDadosRPI import extrair_bloco
import os

def dados_arquivos(caminho_arquivo):
    # Abrir o arquivo txt
    with open(caminho_arquivo, "r", encoding="iso-8859-1") as arquivo:
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
            if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
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
    if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
        # Adicionamos o último bloco à lista de blocos
        lista_blocos.append(texto_bloco)
        
    return lista_blocos

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
