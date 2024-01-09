import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import requests as req
from datetime import datetime
import logging


def APIToParquet(endpoint: str):
    response = req.get(endpoint)

    pipe_options = PipelineOptions()
    dic = response.json()

    dic = dic["USDBRL"]

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

            print("Schema - 200 OK")

            return beam_schema

        except Exception as Err:
            print(f"Schema - 500 Error >>>> {Err}")

    try:
        FileSchema = ParquetSchemaLoad(dic)
        logging.info("Iniciando pipeline")
        with beam.Pipeline(options=pipe_options) as pipe:
            input_pcollection = (
                pipe
                | "Create" >> beam.Create([dic])
                | "WriteToParquet"
                >> beam.io.WriteToParquet(
                    file_path_prefix=f"{output_path}dolar_today_{CurrentTimestampStr()}",
                    file_name_suffix=".parquet",
                    schema=FileSchema,
                    row_group_buffer_size=1024 * 1024,
                    record_batch_size=1000,
                )
            )
        print("Pipeline Execution - 200 OK")
    except Exception as err:
        print(f"Pipeline Execution - 500 Error >>>> {err}")


APIToParquet("https://economia.awesomeapi.com.br/last/USD-BRL")
