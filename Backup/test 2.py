from unidecode import unidecode

def find_and_extract_info(filename):
    # Lista para armazenar as informações encontradas
    extracted_info = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Verifica se a linha contém o trecho "UNIVERSIDADE DE BRASILIA"
            if "UNIVERSIDADE DE BRASILIA" in unidecode(line).upper():
                # Verifica as linhas próximas, anteriores e posteriores
                for offset in range(-2, 3):  # Vasculha 2 linhas antes e 2 linhas depois
                    index = i + offset
                    if 0 <= index < len(lines):
                        # Copia o conteúdo das linhas que começam com os trechos específicos
                        if lines[index].startswith(("(21)", "(22)", "(71)", "(co)", "(Cd)")):
                            extracted_info.append(lines[index].strip())
                            
                # Atualiza o valor de i para pular as próximas linhas já que já foram verificadas
                i += 4

            i += 1

    return extracted_info

# Nome do arquivo txt
filename = '/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt'

# Chama a função e obtém as informações encontradas
informations = find_and_extract_info(filename)

# Imprime as informações
for info in informations:
    print(info)




exit()
def find_and_extract_info(filename):
    # Lista para armazenar as informações encontradas
    extracted_info = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            # Verifica se a linha contém o trecho "UNIVERSIDADE DE BRASILIA"
            if "UNIVERSIDADE DE BRASILIA" in line:
                # Verifica as linhas próximas, anteriores e posteriores
                for offset in range(-2, 3):  # Vasculha 2 linhas antes e 2 linhas depois
                    index = i + offset
                    if 0 <= index < len(lines):
                        # Copia o conteúdo das linhas que começam com os trechos específicos
                        if lines[index].startswith(("(21)", "(22)", "(71)", "(co)", "(Cd)")):
                            extracted_info.append(lines[index].strip())

    return extracted_info

# Nome do arquivo txt
filename = '/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt'

# Chama a função e obtém as informações encontradas
informations = find_and_extract_info(filename)
print(informations)
# Imprime as informações
for info in informations:
    print(info)




exit()
with open("/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt", "r") as arquivo:
    linhas = arquivo.readlines()

def achar_linhas(input1, input2):
    # Procurar pelo termo "UNIVERSIDADE DE BRASÍLIA" no arquivo
    for i, linha in enumerate(linhas):
        if "UNIVERSIDADE DE BRASILIA" in linha:
            # Procurar pelas posições anteriores até encontrar os termos "(21)", "(22)", "(71)", "(co)", e "(Cd)"
            termos_anteriores = []
            for j in range(i - 1, -1, -1):
                if any(term in linhas[j] for term in [input1, "(22)", "(71)", "(co)", "(Cd)"]):
                    termos_anteriores.append(linhas[j].strip())
            termos_anteriores.reverse()  # Revert the list to maintain the original order
            
            # Imprimir os termos encontrados
            for termo in termos_anteriores:
                print(termo)
                
            return termos_anteriores

data_dep = achar_linhas("(21)", "(71)")
n_protecao = achar_linhas("(Cd)", "(22)")
codigo = achar_linhas("(71)", "(21)")
