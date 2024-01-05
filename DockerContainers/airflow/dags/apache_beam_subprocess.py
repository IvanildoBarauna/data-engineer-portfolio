from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from apache_beam.options.pipeline_options import PipelineOptions
import yaml


default_args = {
    'owner': 'Ivanildo Barauna',
    'depends_on_past': False,
    'start_date': "2023-01-01",
    'retries': 0,
    'email_on_failure': False,
    'email_on_retry': False,
}

job = DAG(
    dag_id='apache_beam_subprocess',
    default_args=default_args,
    description='',
    schedule='* * * * *',  # Pode definir uma programação apropriada
    catchup=False,
    tags=['APACHE_BEAM']
)

# Função que executa o script Apache Beam
def run_beam_script():
    import subprocess
    subprocess.run(["python3", "-m", "apache_beam.examples.wordcount",
                    "--input=/opt/airflow/mybucket/youtubers_df.csv",
                    "--output=/opt/airflow/mybucket/output",
                    "--runner=DirectRunner",
                    "--job_endpoint=embed",
                    "--environment_type=DOCKER",
                    "--environment_config=apache/beam_python3.7_sdk:2.48.0"])

start = EmptyOperator(task_id ="starting_pipeline")

# Use o operador PythonOperator para executar o script
run_beam_task = PythonOperator(
    task_id='run_beam_script',
    python_callable=run_beam_script,
    dag=job,
)

end = EmptyOperator(task_id ="end_pipeline")

# Defina a ordem de execução da tarefa
start >> run_beam_task >> end
