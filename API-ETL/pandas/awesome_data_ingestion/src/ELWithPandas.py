import datetime


class AwesomeAPI():
    """
    Objective: Extract and Load Data From API
    API Reference: https://docs.awesomeapi.com.br/

    Examples:

        ## Currency

        your_dictionary = AwesomeAPI().Currency.GetData("USD", "BRL")
        your_file = AwesomeAPI().Currency.GetAndExportData("USD", "BRL", "out_path")
    """

    def PromptMessage(msg: str):
        return print(f'LOG: {datetime.datetime.now()}: {msg}')

    class Currency():

        # Use staticmethod for call class without instance
        @staticmethod
        def GetData(currency: str, currency_for_compare: str):

            def DataRequest(curr: str = currency, curr_com: str = currency_for_compare) -> dict:
                # Modules
                import requests as req
                # url_api
                url_prefix = "https://economia.awesomeapi.com.br/last/"
                # make and call reponse URL
                url_get = f"{url_prefix}{curr}-{curr_com}"

                try:
                    call = req.get(url_get)
                    if call.ok:
                        AwesomeAPI.PromptMessage(f"GetRequest Done: {call}")
                    else:
                        AwesomeAPI.PromptMessage(
                            f"GetRequest StatusCode: {req.get(url_get).status_code}")
                except Exception as e:
                    AwesomeAPI.PromptMessage(f"GetRequest Error: {e}")

                return call.json()[f'{curr}{curr_com}']

            # transform response in dictionary
            json_data = DataRequest()

            # Dicionary mapping fields
            try:
                dic = {
                    "parity": f"{currency}-{currency_for_compare}",
                    "friendly_name": json_data["name"],
                    "price": json_data["bid"],
                    "day_over_day": json_data["varBid"],
                    "day_over_day_pct": json_data["pctChange"],
                    "higher": json_data["high"],
                    "lower": json_data["low"],
                    "updated_at": json_data["create_date"]
                }
                AwesomeAPI.PromptMessage("MappingFields: Done")
            except Exception as e:
                AwesomeAPI.PromptMessage(f"MappingFields: Error {e}")

            return dic

        @staticmethod
        def GetAndExportData(currency: str, currency_for_compare: str, output_path: str, FileName: str, NewFile: bool = True):
            import pandas as pd

            # current_timestamp for new file_name the each extract
            current_timestamp = datetime.datetime.now().timestamp().__str__().replace(".", "")
            values = AwesomeAPI.Currency.GetData(
                currency, currency_for_compare)
            # Create Pandas DataFrame
            df = pd.DataFrame([values])

            df['timestamp_execution'] = datetime.datetime.now()
            # CSV Generate
            try:
                def FinalPath() -> str:
                    if NewFile:
                        return f'{output_path}{FileName}_{current_timestamp}.csv'
                    return f'{output_path}{FileName}.csv'
                path = FinalPath()
                df.to_csv(path)
                AwesomeAPI.PromptMessage(
                    f"CSV File loaded in {path} with success.")
            except Exception as e:
                AwesomeAPI.PromptMessage(f"CSVFile: Error {e}")
