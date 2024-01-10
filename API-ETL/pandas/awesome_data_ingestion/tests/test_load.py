import pandas as pd
import os


def get_latest_file(directory):
    # Lista todos os arquivos no diretório
    files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))
    ]

    # Retorna None se não houver arquivos no diretório
    if not files:
        return None

    # Obtém o caminho do último arquivo modificado
    latest_file = max(files, key=os.path.getmtime)

    return latest_file


diretorio = "/Users/ivsouza/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/"
ultimo_arquivo = get_latest_file(diretorio)

if ultimo_arquivo:
    print(f"ReadingFile >>>>: {ultimo_arquivo}")
    df = pd.read_parquet(ultimo_arquivo)
else:
    print("NoFiles for read")
