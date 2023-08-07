# importar o módulo unicodedata
import unicodedata

# definir uma função para remover os acentos de uma string
def remover_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# abrir um arquivo txt específico, com dados
arquivo = open("/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt", "r")

# criar a lista de dados vazia
dados = []

# buscar cada linha pelo início "(21)"
bloco = [] # lista para armazenar as linhas entre cada (21)
for linha in arquivo:
    if linha.startswith("(21)"): # se a linha começa com (21)
        if bloco: # se o bloco não está vazio
            dados.append(bloco) # adicionar o bloco à lista de dados
        bloco = [linha] # iniciar um novo bloco com a linha atual
    else: # se a linha não começa com (21)
        bloco.append(linha) # adicionar a linha ao bloco atual

# verificar se a palavra UNIVERSIDADE DE BRASILIA está em qualquer linha do bloco, ignorando os acentos
dados = [] # lista vazia para armazenar os dados encontrados
for b in bloco:
    for l in b:
        if remover_acentos("UNIVERSIDADE DE BRASILIA") in remover_acentos(l): # se a palavra está na linha, sem considerar os acentos
            dados.append(b) # adicionar o bloco à lista de dados
            break # sair do loop interno

# fechar o arquivo
arquivo.close()

# imprimir os dados encontrados
for d in dados:
    print("".join(d)) # imprimir cada bloco como uma string
