import apache_beam as beam
import pyarrow
import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
data = response.json()

# fields = []

# for field in data:
#     fields += [(field, pyarrow.string())]

# print(type(fields))


# # Define o esquema
# parquet_schema = pyarrow.schema([("name", pyarrow.binary()), ("age", pyarrow.int64())])

# with beam.Pipeline() as p:
#     records = (
#         p
#         | "Read"
#         >> beam.Create([{"name": "foo", "age": 10}, {"name": "bar", "age": 20}])
#         | "Write"
#         >> beam.io.WriteToParquet(
#             file_path_prefix="./teste",
#             file_name_suffix=".parquet",
#             schema=parquet_schema,
#         )
#     )


def AvroSchemaLoad(element: dict):
    import pyarrow

    api_header = list(element.keys())

    schema = []

    for field in api_header:
        schema += [(field, pyarrow.string())]

    beam_schema = pyarrow.schema(schema)

    return beam_schema


print(AvroSchemaLoad(data))
