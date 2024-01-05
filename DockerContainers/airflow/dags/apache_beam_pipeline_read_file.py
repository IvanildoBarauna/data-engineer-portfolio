# Generic Imports
import os
from datetime import datetime
# AirFlow Imports teste de envio para o Git
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
# ApacheBeam Imports
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
# Database imports
import psycopg2
from psycopg2 import sql

current_timestamp = datetime.now()
current_timestamp = current_timestamp.strftime(("%Y%m%d%H%M%S"))

# PythonTasks
def pyReadAndWriteNewFile(input_file: str):
    # File Instance
    bucket_path = '/opt/airflow/mybucket'
    input_file = f"{bucket_path}/StudentsPerformance.csv"
    name_file = os.path.basename(input_file).split('.')[0]
    output_path = f'/opt/airflow/mybucket/{name_file}/'

    db_params =  { 
        'dbname': 'airflow',
        'user': 'airflow',
        'password': 'airflow',
        'host': 'host.docker.internal',
        'port': '5432'
    }

    # Pipe instance
    pipe_options = PipelineOptions()
    pipe_options.view_as(
        beam.options.pipeline_options.SetupOptions).save_main_session = True
    
    def process_csv(row):
        fields = row.split(',')
        return {
            'gender': fields[0],
            'race': fields[1],
            'parental_level': fields[2],
            'lunch': fields[3],
            'test_preparation': fields[4],
            'math_score': fields[5],
            'reading_score': fields[6],
            'writing_score': fields[7]
        }
    
    def insert_data_to_postgres(element):
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        schema_name = "devel"
        table_name = "student_scores"
        insert_query = sql.SQL("INSERT INTO {}.{} ({}) VALUES ({})").format(
            sql.Identifier(schema_name),
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, element.keys())),
            sql.SQL(', ').join(map(sql.Placeholder, element.keys()))
        )

        truncate_query = sql.SQL(f"TRUNCATE TABLE {schema_name}.{table_name}")
        cursor.execute(truncate_query)
        cursor.execute(insert_query, element)
        conn.commit()
        conn.close()

    # Pipe Definitions
    with beam.Pipeline(options=pipe_options) as pColl:
        (pColl
            | 'ReadFile' >> beam.io.ReadFromText(input_file, skip_header_lines=0)
            | 'ParseCSV' >> beam.Map(process_csv)
            | 'InsertDataToPostgreSQL' >> beam.ParDo(insert_data_to_postgres)
            )
            
# AirFlow DAG Instance

with DAG(
    dag_id='apache_beam_pipeline_read_file' ,
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['APACHE_BEAM']
) as dag:
    """
    Esta é uma DAG de exemplo do Apache Beam Pipeline para leitura de arquivos.
    Proprietário: Ivanildo Barauna
    """
    # AirFlow Tasks Instance
    StartDummy = EmptyOperator(task_id='starting_pipeline')

    ReadAndWriteNewFile = PythonOperator(
        task_id="ReadAndWriteNewFile",
        python_callable=pyReadAndWriteNewFile,
        op_args=['/opt/airflow/mybucket/StudentsPerformance.csv']
    )

    EndDummy = EmptyOperator(task_id='final_pipeline')

# AirFlow tasks
StartDummy >> ReadAndWriteNewFile >> EndDummy
