import requests as req
import json as js
import datetime

current_timestamp = datetime.datetime.now().timestamp().__str__()
current_timestamp = current_timestamp.replace(".", "")

output_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/python/src/__databases/output/dolar/"
url_prefix = "https://economia.awesomeapi.com.br/last/"
curr = "USD"
curr_compare = "BRL"
parity = f"{curr}{curr_compare}"
url_get = f"{url_prefix}{curr}-{curr_compare}"

call = req.get(url_get)
json = call.json()[parity]

dic = {
    "created_at": json["create_date"],
    "parity": f"{curr}-{curr_compare}",
    "friendly_name": json["name"],
    "price": json["bid"],
    "day_over_day": json["varBid"],
    "day_over_day_pct": json["pctChange"],
    "higher": json["high"],
    "lower": json["low"],
}


""" 
Escrever aqui o código que lê esses dados do Dic
via pandas e manda para um arquivo
"""