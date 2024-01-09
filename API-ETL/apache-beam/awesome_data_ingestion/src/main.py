# from etl.extract import APIToParquet
import pyarrow.parquet as pq

# def main():
# APIToParquet("https://economia.awesomeapi.com.br/last/USD-BRL")

# if __name__ == "__main__":
#     main()
caminho_do_arquivo_parquet = "/Users/ivsouza/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/dolar_today_1704806850-00000-of-00001.parquet"

tabela_parquet = pq.read_table(caminho_do_arquivo_parquet)

print(tabela_parquet)
