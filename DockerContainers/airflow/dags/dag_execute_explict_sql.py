## Importação de dependências: Do airFlow Importar a DAG
from airflow import DAG
## Importação de dependências: Do airFlow Operators Python Importar o operador de Python
from airflow.providers.postgres.operators.postgres import PostgresOperator
## Python com PostGres

## DAG Instance
default_args={
    'owner': "Ivanildo Barauna de Souza Junior",
    'depends_on_past': True,
    'start_date': "2023-10-01",
    'email_on_failure': False,
    'email_on_retry': False,    
    'retries': 2,
    }

job = DAG(
    dag_id = 'execute_sql_explicit_on_dag',
    default_args=default_args,
    description='This Job Execute SQL on PostGres',
    schedule='*/5 * * * * ',
    catchup=False,
    template_searchpath='/opt/airflow/sql'
    )


insert_table_clients =PostgresOperator(
        task_id='insert_table_clients',
        postgres_conn_id= 'lake_conn',
        sql = '/data_raw/insert_table_clients.sql',
        dag = job
    )

for i in range(10000):
    insert_table_clients 




