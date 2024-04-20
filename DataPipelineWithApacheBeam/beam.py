import apache_beam as beam
import datetime
from apache_beam.options.pipeline_options import PipelineOptions

current_timestamp = datetime.datetime.now().timestamp().__str__()
current_timestamp = current_timestamp.replace(".", "")

output_folder = "./output/databases"
input_file = f"{output_folder}/train.csv"
input_file_arr = input_file.split("/")
file_name = input_file_arr[len(input_file_arr)-1]
file_name = file_name.split(".")[0].lower() + "_"

output_path = f"{output_folder}/output/" + file_name

# Pipe instance
pipe_options = PipelineOptions()
pipe_options.view_as(
    beam.options.pipeline_options.SetupOptions).save_main_session = True

with beam.Pipeline(options=pipe_options) as pipe:
    (pipe
        | 'ReadFile' >> beam.io.ReadFromText(input_file)
        | 'WriteOutput' >> beam.io.WriteToText(file_path_prefix=f'{output_path}{current_timestamp}', file_name_suffix='.avro', num_shards=0)
    )
    
    
    
#### Schema with pyarrow
import pyarrow

def DefaultQuotesAPISchema():
    api_header = [
        "code",
        "codein",
        "name",
        "high",
        "low",
        "varBid",
        "pctChange",
        "bid",
        "ask",
        "timestamp",
        "create_date"]

    schema = []
    for field in api_header:
        schema += [(field, pyarrow.string())]

    return pyarrow.schema(schema)