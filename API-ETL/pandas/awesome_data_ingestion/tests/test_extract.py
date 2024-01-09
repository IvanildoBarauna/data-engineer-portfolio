import requests

endpoint = "https://economia.awesomeapi.com.br/last/USD-BRL"

dic = requests.get(endpoint).json()


def CurrencyDictionary(data: dict) -> dict:
    arr_endpoint = endpoint.split("/")
    params = arr_endpoint[len(arr_endpoint) - 1]
    params = params.replace("-", "")

    return data[params]


print(CurrencyDictionary(dic))
