from airflow import DAG
from airflow.operators.python import PythonOperator

# Instanciamento de DAG
## OBS: Equivalente aos JOBS do Pentaho
job = DAG(
    dag_id='example_python_simple',
    default_args={
        'owner': "Ivanildo Barauna",
        'depends_on_past': False,
        'start_date': "2023-01-01",
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
    },
    description='This is my fisrt Dag on Apache Air Flow',
    schedule=None,  #  https://crontab.guru/#5_4_*_*_sun
    catchup=False,  # Impede a execução retroativa das tarefas
    tags = ['PYTHON']
)

## Funções de Extração, Carregamento e Load que viram tasks para as DAGS
## Equivalente aas transformações no Pentaho
def fx_extract(): 
    print("This is a task for extract task..")

def fx_transform(): 
    print("This is a task for transform task..")

def fx_target_load(): 
    print("This is a task for load task..")

# Instanciamento de TASKS
## OBS: Equivalente as transformações do Pentaho que ficam dentro dos jobs
extract_task = PythonOperator(
    task_id='fx_extract',
    python_callable=fx_extract,
    dag=job,
)

transform_task = PythonOperator(
    task_id='fx_transform',
    python_callable=fx_transform,
    dag=job,

)

load_task = PythonOperator(
    task_id='fx_target_load',
    python_callable=fx_target_load,
    dag=job,
)

extract_task >> transform_task >> load_task



