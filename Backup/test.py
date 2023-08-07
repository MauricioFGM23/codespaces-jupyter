from unidecode import unidecode  # Certifique-se de ter o pacote 'unidecode' instalado
import os

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

    # Abrir o arquivo "Resultados.txt" em modo de append (adicionar)
    with open("/workspaces/codespaces-jupyter/RPISpider/resultados/Resultados.txt", "a", encoding="utf-8") as resultados_arquivo:
        # Percorrer todas as linhas do arquivo
        for linha in linhas:
            if linha.startswith("(21)"):
                # Se encontrarmos um novo bloco, verificamos se o texto anterior possui "UNIVERSIDADE DE BRASILIA"
                if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
                    # Gravamos o texto do bloco no arquivo "Resultados.txt"
                    resultados_arquivo.write(texto_bloco)

                # Reiniciamos o texto do bloco e marcamos que estamos dentro de um novo bloco
                dentro_do_bloco = True
                texto_bloco = linha
            else:
                # Se estivermos dentro de um bloco, continuamos a acumular o texto
                if dentro_do_bloco:
                    texto_bloco += linha

        # Verificamos o último bloco após sair do loop
        if dentro_do_bloco and "UNIVERSIDADE DE BRASILIA" in unidecode(texto_bloco).upper():
            # Gravamos o último bloco no arquivo "Resultados.txt"
            resultados_arquivo.write(texto_bloco)

    print("Os dados foram gravados em 'Resultados.txt'.\n")


if __name__ == "__main__":

    
    pasta = "/workspaces/codespaces-jupyter/RPISpider/downloads"
    arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.txt')]

        # Aplica a função em cada arquivo .txt encontrado.
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        print(f"Lendo o arquivo: {arquivo}")
        dados_arquivos(caminho_arquivo)