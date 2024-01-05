# from pyspark.sql.functions import current_timestamp, count, asc, desc, col
# import datetime
    # from pyspark.sql import SparkSession


    

input_file = "/Users/ivbarauna/repos/bitbucket_mycodes/python/src/__databases/train.csv"

def GetOutputFileName(file: str = input_file):
    current_timestamp = datetime.datetime.now().timestamp().__str__()
    current_timestamp = current_timestamp.replace(".", "")

    input_file_arr = file.split("/")
    file_name = input_file_arr[len(input_file_arr)-1]
    output_file_name = file_name.split(
        ".")[0].lower() + "_" + current_timestamp

    output_folder = file.replace(file_name, "") + "output/"

    return {"folder": output_folder, "file":output_file_name}

output_path =""
file_output_name = ""

output_path = GetOutputFileName(file=input_file)["folder"]
file_output_name = GetOutputFileName(file=input_file)["file"]

# Carregar os dados para um objeto do spark
df = my_spark_session.read.csv(input_file, header=True, inferSchema=True)

# Mostrar o schema dos dados
# df.printSchema()

# Quantidade de linhas
# df.count()

# Selecionar colunas
# df = df.select(
#     'title', 'date_added', 'country', 'director', 'rating'
# )

# Adicionar uma nova coluna
df = df.withColumn('timestamp_execution', current_timestamp())

# realizando filtros no dataframe
df_filtered = df.filter(df.country == "United States")

df_filtered = df_filtered.select('show_id', 'country', 'timestamp_execution')

# df_filtered.show()

# df_group_by_country = df_filtered.groupBy('country').count()
# df_group_by_country.show()

# df_group_by_director = df_filtered.groupBy('director').count()
# df_group_by_director.show()

# df.createOrReplaceTempView('vw_teste')

# df_sql = my_spark_session.sql(""" 
#                     select 
#                         show_id, title 
#                     from vw_teste
#                     where not director is null
#                     and not country is null
#                     and not cast is null
#                      """)


# # Criando o join entre tabelas
# df_sql.join(df_filtered, df_sql.show_id == df_filtered.show_id, "inner")\
#     .select(df_sql.show_id, df_sql.title, df_filtered.country) \
#     .show(truncate=False)
    
df_filtered.write.csv(f"{output_path}{file_output_name}")
