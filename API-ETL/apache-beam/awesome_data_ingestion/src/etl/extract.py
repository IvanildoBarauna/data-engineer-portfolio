import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import requests as req
from datetime import datetime
from .logs import ConsoleInfo


def APIToParquet(endpoint: str):
    output_path = "/Users/ivsouza/repos/data-engineer-portfolio/API-ETL/apache-beam/awesome_data_ingestion/data/external/kaggle/"
    pipe_options = PipelineOptions(["--runner", "Direct"])

    def CurrencyDictionary() -> dict:
        response = req.get(endpoint)
        dic = response.json()
        arr_endpoint = endpoint.split("/")
        params = arr_endpoint[len(arr_endpoint) - 1]
        params = params.replace("-", "")

        return dic[params]

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

            ConsoleInfo("Schema - 200 OK")

            return beam_schema

        except Exception as Err:
            ConsoleInfo(f"Schema - 500 Error >>>> {Err}")

    try:
        dic = CurrencyDictionary()
        FileSchema = ParquetSchemaLoad(dic)
        ConsoleInfo("Iniciando pipeline")
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
        ConsoleInfo("Pipeline Execution - 200 OK")
    except Exception as err:
        ConsoleInfo(f"Pipeline Execution - 500 Error >>>> {err}")
