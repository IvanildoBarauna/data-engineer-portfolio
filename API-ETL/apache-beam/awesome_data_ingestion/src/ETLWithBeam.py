import requests as req
import json as js
import apache_beam as beam
import datetime
from apache_beam.options.pipeline_options import PipelineOptions

current_timestamp = datetime.datetime.now().timestamp().__str__()
current_timestamp = current_timestamp.replace(".", "")

output_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/python/src/__databases/output/dolar/"
url_prefix = "https://economia.awesomeapi.com.br/last/"
curr = "USD"
curr_compare = "BRL"
parity = f"{curr}{curr_compare}"
url_get = f"{url_prefix}{curr}-{curr_compare}"

call = req.get(url_get)
json = call.json()[parity]

dic = {
    "created_at": json["create_date"],
    "parity": f"{curr}-{curr_compare}",
    "friendly_name": json["name"],
    "price": json["bid"],
    "day_over_day": json["varBid"],
    "day_over_day_pct": json["pctChange"],
    "higher": json["high"],
    "lower": json["low"],
}


print(json)

def dict_to_values_list(element):
    return list(element.values())


# Pipe instance
pipe_options = PipelineOptions()
pipe_options.view_as(
    beam.options.pipeline_options.SetupOptions).save_main_session = True

# with beam.Pipeline(options=pipe_options) as pipe:
#     (pipe
#         | 'ReadDic' >> beam.Create(([dic]))
#         | "FlattenDict" >> beam.FlatMap(dict_to_key_value)
#         # | "Print" >> beam.Map(lambda x: print(x))
#         | 'WriteOutput' >> beam.io.WriteToText(file_path_prefix=f'{output_path}_dolar_today_{current_timestamp}', file_name_suffix='.csv', num_shards=0)
#     )

with beam.Pipeline(options=pipe_options) as pipe:
    input_pcollection = (
        pipe
        | "Create" >> beam.Create([dic])
        | "ValuesList" >> beam.Map(dict_to_values_list)
    )

    # Escrevendo o PCollection em um arquivo CSV
    input_pcollection | "WriteToCSV" >> beam.io.WriteToText(
        f'{output_path}_dolar_today_{current_timestamp}'
        , file_name_suffix=".csv"
        , header="created_at,parity,friendly_name,price,day_over_day,day_over_day_pct,higher,lower"
        ,num_shards=1
        , shard_name_template="")
