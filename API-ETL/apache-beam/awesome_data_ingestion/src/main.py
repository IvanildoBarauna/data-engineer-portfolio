from etl.extract import ExtractDataAPI
import os

# import requests

api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
path = f"/Users/{os.getenv('USER')}/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/"

NewExtract = ExtractDataAPI(endpoint=api, output_path=path)

NewExtract.PipelineRun()

# response = NewExtract.APIToDicionary()
# json_data = response["responseData"]
# params = response["params"]

# for item in enumerate(params):
#     print(item)
