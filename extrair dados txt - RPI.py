from unidecode import unidecode

def find_and_extract_info(filename):
    # Lista para armazenar as informações encontradas
    extracted_info = []

    # Indicadores que queremos buscar
    indicators = ["(21)", "(22)", "(71)", "(co)", "(Cd)"]

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            line = lines[i]
            # Verifica se a linha contém o trecho "UNIVERSIDADE DE BRASILIA" ou "UNIVERSIDADE DE BRASÍLIA" (insensível a acentos)
            if "UNIVERSIDADE DE BRASILIA" in unidecode(line).upper():
                # Verifica as linhas próximas, anteriores e posteriores
                for offset in range(-2, 3):  # Vasculha 2 linhas antes e 2 linhas depois
                    index = i + offset
                    if 0 <= index < len(lines):
                        # Verifica cada um dos indicadores e extrai as informações se encontrados
                        
                        for indicator in indicators:
                            if lines[index].startswith(indicator):
                                extracted_info.append(lines[index].strip())
                                break  # Se encontrou um indicador, não é necessário continuar procurando

                # Atualiza o valor de i para pular as próximas linhas já que já foram verificadas
                i += 4

            i += 1

    return extracted_info

# Nome do arquivo txt
FILENAME  = '/workspaces/codespaces-jupyter/RPISpider/downloads/P2710.txt'

# Chama a função e obtém as informações encontradas
informations = find_and_extract_info(FILENAME)

# Imprime as informações
for info in informations:
    print(info)
