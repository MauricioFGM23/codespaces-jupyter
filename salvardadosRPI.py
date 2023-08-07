import pandas as pd

def extrair_bloco(planilha, entrada_dados):
    data_dict = {}
    for line in entrada_dados:
        if line.startswith("(21)"):
            data_dict["(21) numero da proteção"] = line[5:].strip()
        elif line.startswith("(22)"):
            data_dict["(22) data do depósito"] = line[5:].strip()
        elif line.startswith("(71)"):
            data_dict["(71) titulares"] = line[5:].strip()
        elif line.startswith("(72)"):
            data_dict["(72) autores"] = line[5:].strip()
        elif line.startswith("(54)"):
            data_dict["(54) título"] = line[5:].strip()
        elif line.startswith("(co)"):
            data_dict["(co) comentário"] = line[5:].strip()
        elif line.startswith("(Cd)"):
            data_dict["(Cd) código da exigência"] = line[5:].strip()

    try:
        # Load the existing data from the "dadosRPI.csv" file
        df = pd.read_excel(planilha)
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with the extracted data
        df = pd.DataFrame([data_dict])
    else:
        # Append the data from the current block to the existing DataFrame
        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)

    # Save the DataFrame back to a new CSV file with encoding 'utf-8'
    #filename = planilha.split("/")[-1]  # Extract the filename from the path
    df.to_excel(planilha, index=False)

data_block = [
    "(21) BR 11 2022 020846-4 A2",
    "(22) 15/04/2021",
    "(30) 15/04/2020 US 63/010,185",
    "(51) A61K 38/20 (2006.01), A61P 35/00 (2006.01), C07K 14/55 (2006.01), C07K 14/715 (2006.01), C12N 15/62 (2006.01)",
    "(54) AGENTES IMUNOESTIMULADORES EM COMBINAÇÃO COM INIBIDORES DE ANGIOGÊNESE",
    "(71) ALKERMES PHARMA IRELAND LIMITED (IE) ; CLOVIS ONCOLOGY, INC. (US)"
]

planilha = "/workspaces/codespaces-jupyter/RPISpider/resultados/Dados RPI.xlsx"
extrair_bloco(planilha, data_block)
