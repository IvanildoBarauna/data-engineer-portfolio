from etl.extract import APIToParquet

def main():
    APIToParquet("https://economia.awesomeapi.com.br/last/USD-BRL")
    
if __name__ == "__main__":
    main()


    
