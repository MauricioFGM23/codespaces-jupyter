import os
import chardet
import codecs

input_folder = '/workspaces/codespaces-jupyter/RPISpider/downloads/'

print("Iniciando conversão de codificação para utf-8!!!\n")

def convert_to_utf8(input_file, output_file):
    # Detecta a codificação do arquivo de entrada
    with open(input_file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
    input_encoding = result['encoding']

    # Realiza a conversão de codificação
    with codecs.open(input_file, 'r', encoding=input_encoding, errors='ignore') as source_file:
        content = source_file.read()
    
    with codecs.open(output_file, 'w', encoding='utf-8') as target_file:
        target_file.write(content)

# Substitua o caminho da pasta de entrada conforme necessário

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(input_folder, filename)  # Mesmo nome de arquivo
        print(filename)
        convert_to_utf8(input_file_path, output_file_path)
print ("\nConversão de condificação concluída!!!\n")