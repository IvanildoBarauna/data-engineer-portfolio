import apache_beam as beam
from etl.beam_config.PipelineConfiguration import DefaultPipeConfig
import requests as req
from datetime import datetime

def APIToParquet(endpoint: str):
    
    response = req.get(endpoint)

    pipe_options = DefaultPipeConfig()
    dic = response.json()

    output_path = "../../data/external/"

    def ts() -> str:
        current = datetime.now().timestamp()
        return current.__str__().replace(".", "")

    def dict_to_values_list(element):
            return list(element.values())

    with beam.Pipeline(options=pipe_options) as pipe:
        input_pcollection = (
            pipe
            | "Create" >> beam.Create([dic])
            | "ValuesList" >> beam.Map(dict_to_values_list)
            | "WriteToCSV" >> beam.io.WriteToText(
                f'{output_path}_dolar_today_{ts()}'
                , file_name_suffix=".csv"
                ## Passar o header como variável, recuperando os keys json retornado
                , header="created_at,parity,friendly_name,price,day_over_day,day_over_day_pct,higher,lower"
                ,num_shards=1
                , shard_name_template="")
        )

