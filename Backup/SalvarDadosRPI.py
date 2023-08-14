import pandas as pd

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

