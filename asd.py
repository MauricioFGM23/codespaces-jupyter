from unidecode import unidecode

caminho_arquivo = "/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt"
dados = []

# Abrir o arquivo txt
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    # Ler todas as linhas do arquivo
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
    print(bloco.strip())  # strip() para remover espaços em branco extras (quebras de linha)
