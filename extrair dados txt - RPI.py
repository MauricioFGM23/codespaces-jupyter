from unidecode import unidecode
import os

dados = []
def dados_arquivos(caminho_arquivo):
    # Abrir o arquivo txt
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        # Ler todas as linhas do arquivo
        print(f"Conteúdo do arquivo '{caminho_arquivo}': \n")
        linhas = arquivo.readlines()

    # Variável para indicar se estamos dentro de um bloco de texto com "(21)"
    dentro_do_bloco = False

    # Variável para armazenar o texto do bloco atual
    texto_bloco = ""

    # Percorrer todas as linhas do arquivo
    for linha in linhas:
        if linha.startswith("(21)"):
            # Se encontrarmos um novo bloco, verificamos se o texto anterior possui "UNIVERSIDADE DE BRASÍLIA"
            if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
                dados.append(texto_bloco)
            
            # Reiniciamos o texto do bloco e marcamos que estamos dentro de um novo bloco
            dentro_do_bloco = True
            texto_bloco = linha
        else:
            # Se estivermos dentro de um bloco, continuamos a acumular o texto
            if dentro_do_bloco:
                texto_bloco += linha

    # Verificamos o último bloco após sair do loop
    if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
        dados.append(texto_bloco)

    # Imprimimos os dados encontrados
    for bloco in dados:
        print(bloco.strip(),"\n")  # strip() para remover espaços em branco extras (quebras de linha)
    print ("\n")
    return dados

def aplicar_funcao_em_arquivos_txt(pasta):
    # Lista todos os arquivos no diretório informado.
    arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.txt')]

    # Aplica a função em cada arquivo .txt encontrado.
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        print(f"Lendo o arquivo: {arquivo}")
        dados_arquivos(caminho_arquivo)

if __name__ == "__main__":

    pasta = "/workspaces/codespaces-jupyter/RPISpider/downloads/"
    aplicar_funcao_em_arquivos_txt(pasta)
    #print(dados)