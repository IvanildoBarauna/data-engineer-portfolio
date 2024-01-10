import pyarrow.parquet as pq

file_path = "/Users/ivsouza/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/dolar_today_1704919030-00000-of-00001.parquet"

pq.read_table(file_path)
