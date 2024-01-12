import requests

api = "https://economia.awesomeapi.com.br/last/USD-BRL"


class ExtractDataAPI:
    def __init__(self, endpoint: str, output_path: str) -> None:
        self.endpoint = endpoint
        self.output_path = output_path
        self.ExtractedFilePath = []
        self.ValidParams = []

    def APIToDicionary(self):
            def ValidListOfParams():
                arr_endpoint = self.endpoint.split("/")
                params = arr_endpoint[len(arr_endpoint) - 1]
                lstParams = params.split(",")
                
                list_of_avaliable = requests.get("https://economia.awesomeapi.com.br/json/available").json()
                
                ValidParams = []
                
                for param in lstParams:
                    if param in list_of_avaliable:
                        ValidParams.append(param.replace("-", ""))
                    else:
                        print(f"Param: {param} is not valid for call")
                
                return ValidParams
            ## Se for válido segue
            
            
            validParams = ValidListOfParams()
            if validParams:
                print(f"Parameters OK >>> {validParams}")
                response = requests.get(self.endpoint)
                if response.ok:
                    print(f"Response OK >>> {response}")
                    return dict(responseData=response.json(), params=validParams)
                else:
                    print(f"Response failed >>> {response}")


api = "https://economia.awesomeapi.com.br/last/USD-BRL"
path = ""

NewExtract = ExtractDataAPI(endpoint=api, output_path=path)
NewExtract.APIToDicionary()
