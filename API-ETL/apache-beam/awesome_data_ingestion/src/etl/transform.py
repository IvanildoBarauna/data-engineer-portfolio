def x():
    import datetime
    
    current_timestamp = datetime.datetime.now().timestamp().__str__()
    current_timestamp = current_timestamp.replace(".", "")

    url_prefix = "https://economia.awesomeapi.com.br/last/"
    curr = "USD"
    curr_compare = "BRL"
    parity = f"{curr}{curr_compare}"
    url_get = f"{url_prefix}{curr}-{curr_compare}"
    
    
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
    
    def dict_to_values_list(element):
        return list(element.values())
    
    pass