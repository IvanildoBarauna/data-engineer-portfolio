import apache_beam as beam
from beam_config.PipelineConfiguration import DefaultPipeConfig
import requests as req
from datetime import datetime
import logging


def APIToParquet(endpoint: str):
    import pyarrow

    response = req.get(endpoint)

    pipe_options = DefaultPipeConfig()
    dic = response.json()

    output_path = "/Users/ivsouza/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/"

    def CurrentTimestampStr() -> str:
        current = datetime.now().timestamp()
        return str(int(current))

    def ParquetSchemaLoad(element: dict):
        import pyarrow

        try:
            api_header = list(element.keys())

            schema = []

            for field in api_header:
                schema += [(field, pyarrow.string())]

            beam_schema = pyarrow.schema(schema)

            logging.info("Schema OK")

            return beam_schema

        except Exception as Err:
            logging.error(f"Schema Error >>>>> {Err}")

    def dict_to_values_list(element):
        return list(element.values())

    try:
        # logging.info("Iniciando geração de arquivo .avro")
        # SchemaLoaded = AvroSchemaLoad(element=dic)
        FileSchema = ParquetSchemaLoad(dic)
        logging.info("Iniciando pipeline")
        with beam.Pipeline(options=pipe_options) as pipe:
            input_pcollection = (
                pipe
                | "Create" >> beam.Create([dic])
                # | "ExtractHeader" >> beam.Map(extract_header)
                | "ValuesList" >> beam.Map(dict_to_values_list)
                # | "PrintData" >> beam.ParDo(lambda element: print(element))
                | "WriteToParquet"
                >> beam.io.WriteToParquet(
                    filename=f"{output_path}dolar_today_{CurrentTimestampStr()}.parquet",
                    schema=FileSchema
                    ## Passar o header como variável, recuperando os keys json retornado
                )
            )
        logging.info("Pipeline executado com sucesso.")
    except Exception as err:
        logging.error(f"Erro ao executar o pipeline: {err}")


APIToParquet("https://economia.awesomeapi.com.br/last/USD-BRL")
