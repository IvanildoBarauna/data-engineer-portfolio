# Apache Beam Dependencies
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Auxiliar Dependencies
import pyarrow
import requests
from datetime import datetime

# Custom Modules
from .logs import ConsoleInfo, WarningInfo


class ExtractDataAPI:
    def __init__(self, endpoint: str, output_path: str) -> None:
        self.endpoint = endpoint
        self.output_path = output_path
        self.pipe_options = PipelineOptions(["--runner", "Direct"])

    def APIToDicionary(self):
        response = requests.get(self.endpoint)

        if response.ok:
            ConsoleInfo(f"Response OK >>> {response}")
            arr_endpoint = self.endpoint.split("/")
            params = arr_endpoint[len(arr_endpoint) - 1]
            listOfParams = params.replace("-", "").split(",")
            return dict(responseData=response.json(), params=listOfParams)
        else:
            WarningInfo(f"Response failed >>> {response}")

    def CurrentTimestampStr(self) -> str:
        current = datetime.now().timestamp()
        return str(int(current))

    def ParquetSchemaLoad(self, element: dict):
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
        response = self.APIToDicionary()
        json_data = response["responseData"]
        params = response["params"]

        FileSchema = self.ParquetSchemaLoad(json_data[params[0]])
        insert_date = self.CurrentTimestampStr()

        for index, param in enumerate(params):
            dic = json_data[param]

            if dic:
                try:
                    ConsoleInfo(
                        f"Starting pipeline {index + 1} of {len(params)} - {param} - Starting!"
                    )
                    with beam.Pipeline(options=self.pipe_options) as pipe:
                        input_pcollection = (
                            pipe
                            | "Create" >> beam.Create([dic])
                            | "WriteToParquet"
                            >> beam.io.WriteToParquet(
                                file_path_prefix=f"{self.output_path}{param}_{insert_date}",
                                file_name_suffix=".parquet",
                                schema=FileSchema,
                            )
                        )
                    ConsoleInfo(
                        f"Pipeline execution OK >> {index + 1} of {len(params)} - {param} - Extracted!"
                    )
                except Exception as err:
                    ConsoleInfo(f"{param} - Pipeline Execution Error >>>  {err}")
