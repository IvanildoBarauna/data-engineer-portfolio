# Módulo para tratamento de strings
import os
# Módulo para uso das DAGs do AirFlow
from airflow import DAG
# Python Operator no AirFlow
from airflow.operators.python import PythonOperator
# Operador de Dummy no AirFlow
from airflow.operators.empty import EmptyOperator
# Importar o módulo do Apache Beam
import apache_beam as beam
# Para instanciar uma nova opção de pipeline
from apache_beam.options.pipeline_options import PipelineOptions
# Recursos de Data e Hora
from datetime import datetime
    

# Configuração padrão da DAG em JSON
default_args = {'owner': 'Ivanildo Barauna',
                'depends_on_past': False,
                'start_date': "2023-01-01",
                'retries': 0,
                'email_on_failure': False,
                'email_on_retry': False,
                }

# Cria e define uma instância de DAG



dag = DAG(
    dag_id='apache_beam_pipeline',
    default_args=default_args,
    description='DAG que lê arquivos de uma pasta e gera arquivos novos como se fossem fotografias a cada 1 minuto',
    schedule=None,  # Defina uma programação apropriada
    catchup=False,
    tags=['APACHE_BEAM'],
)

# Função para chamar o script do Apache Beam


def read_write_file():
    current_timestamp = datetime.now()
    current_timestamp = current_timestamp.strftime(("%Y%m%d%H%M%S"))
    bucket_path = '/opt/airflow/mybucket'
    input_file = f"{bucket_path}/youtubers_df.csv"
    name_file = os.path.basename(input_file).split('.')[0]
    output_path = f'/opt/airflow/mybucket/{name_file}/'

    # Configura as opções do pipeline
    options = PipelineOptions()
    options.view_as(
        beam.options.pipeline_options.SetupOptions).save_main_session = True

    # Define o pipeline Beam
    with beam.Pipeline(options=options) as p:
        (p
         | 'ReadInput' >> beam.io.ReadFromText(input_file)
         | 'WriteOutput' >> beam.io.WriteToText(file_path_prefix=f'{output_path}{current_timestamp}', file_name_suffix='.csv', num_shards=1
                                                )
         )


start = EmptyOperator(task_id="pipeline_start")

# Use o operador PythonOperator para executar o script
read_write_file = PythonOperator(
    task_id='pipeline_running',
    python_callable=read_write_file,
    dag=dag,
)

end = EmptyOperator(task_id="pipeline_end")

# Defina a ordem de execução da tarefa
start >> read_write_file >> end
