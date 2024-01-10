from etl.extract import ExtractDataAPI
import os

api = "https://economia.awesomeapi.com.br/last/USD-BRL"
path = f"/Users/{os.getenv('USER')}/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/"


NewExtract = ExtractDataAPI(endpoint=api, output_path=path)
NewExtract.PipelineRun()

# print(os.get_exec_path())
