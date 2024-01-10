import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import requests as req
from datetime import datetime
from .logs import ConsoleInfo


class ExtractDataAPI:
    def __init__(self, endpoint: str, output_path: str) -> None:
        self.endpoint = endpoint
        self.output_path = output_path
        self.pipe_options = PipelineOptions(["--runner", "Direct"])

    def CurrencyDictionary(self) -> dict:
        response = req.get(self.endpoint)
        dic = response.json()
        arr_endpoint = self.endpoint.split("/")
        params = arr_endpoint[len(arr_endpoint) - 1]
        params = params.replace("-", "")
        return dic[params]

    def CurrentTimestampStr(self) -> str:
        current = datetime.now().timestamp()
        return str(int(current))

    def ParquetSchemaLoad(self, element: dict):
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

    def PipelineRun(self):
        try:
            dic = self.CurrencyDictionary()
            FileSchema = self.ParquetSchemaLoad(dic)
            ConsoleInfo("Iniciando pipeline")
            with beam.Pipeline(options=self.pipe_options) as pipe:
                input_pcollection = (
                    pipe
                    | "Create" >> beam.Create([dic])
                    | "WriteToParquet"
                    >> beam.io.WriteToParquet(
                        file_path_prefix=f"{self.output_path}dolar_today_{self.CurrentTimestampStr()}",
                        file_name_suffix=".parquet",
                        schema=FileSchema,
                    )
                )
            ConsoleInfo("Pipeline Execution - 200 OK")
        except Exception as err:
            ConsoleInfo(f"Pipeline Execution - 500 Error >>>> {err}")
