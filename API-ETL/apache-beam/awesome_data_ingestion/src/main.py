# import ELWithPandas as pipeline
from awesome_data_ingestion.ExtractAndLoadWithPandas import ELWithPandas as pipeline

dic =  pipeline.AwesomeAPI().Currency.GetData("EUR", "BRL")

print(dic)