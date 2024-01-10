import datetime
from airflow import DAG

ts = datetime.datetime.now().timestamp().__str__()
ts = ts.replace(".", "")

# Criando um dicionário
dic = {
    "variables": {
        "proj_id": "",
        "dme1": "",
    },
    "pipeline_id": f"event_cards.PURCHASE_TRANSACTION_{ts}",
    "schedule": "* * * * *"
}

# Exemplo de atribuição de valor
with DAG():
    dag_id = dic["pipeline_id"]
    start_date = "2023-02-01",
    schedule = dic["schedule"]

# Listar chaves
dic.keys()
# Listar valores
dic.values()
# Lista tuplas
dic.items()

meu_dicionario = {
    "registro": "0001",
    "produto": "notebook",
    "modelo": "Macbook",
    "conexões": ["usb-c", "usb", "p2", "hdmi"]
}

## Adicionando uma nova chave e valor no dic
meu_dicionario["perifericos"] = ["teclado", "mouse"]
