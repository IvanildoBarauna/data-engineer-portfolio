import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def FileToDataFrame(file_path: str):
    import pandas as pd

    logging.info("Read file starting")
    df = pd.read_csv(file_path)
    df = df.head(1)
    logging.info("Process file starting")
    dict = df.to_dict("records")
    dict = dict[0]

    for key in dict.keys():
        print(key)
    
FileToDataFrame(
    file_path="./file-source/openpowerlifting.csv"
)