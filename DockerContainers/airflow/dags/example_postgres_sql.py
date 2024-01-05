## Importação de dependências: Do airFlow Importar a DAG
from airflow import DAG
## Importação de dependências: Do airFlow Operators Python Importar o operador de Python
from airflow.providers.postgres.operators.postgres import PostgresOperator
## Python com PostGres
from airflow.operators.python_operator import PythonOperator

## DAG Instance
default_args={
    'owner': "Ivanildo Barauna",
    'depends_on_past': False,
    'start_date': "2023-10-01",
    'email_on_failure': False,
    'email_on_retry': False,    
    'retries': 0,
    }

job = DAG(
    dag_id = 'example_postgres_sql',
    default_args=default_args,
    description='This Job Execute SQL on PostGres',
    schedule=None,
    catchup=False,
    template_searchpath='/opt/airflow/templates',
    tags = ['POSTGRES_DB'] 
    )

create_table_clients =PostgresOperator(
        task_id='create_table_clients',
        postgres_conn_id= 'lake_conn',
        sql = '/sql/create_table_on_data_raw.sql',
        dag = job
    )

insert_table_clients =PostgresOperator(
        task_id='insert_table_clients',
        postgres_conn_id= 'lake_conn',
        sql = '/sql/insert_table_clients.sql',
        dag = job
    )


def MultipleInsert():
    for i in range(100):
        insert_table_clients.execute(context={})
    

LoopTask = PythonOperator(
    task_id='MultipleInsert',
    python_callable=MultipleInsert,  # Remove the parentheses
    dag=job,
)

create_table_clients >> LoopTask








