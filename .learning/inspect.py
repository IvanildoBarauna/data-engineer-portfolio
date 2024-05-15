import inspect
import datetime
import json
import pandas as pd
import os

def start():
    print("função start iniciada")
    middle(1)

def middle(param):
    print("função middle iniciada")
    finish(1)

def finish(param):
    print("função finish iniciada")
    stack = inspect.stack()
    log = []
    for frame in stack:
        log.append( {
            "current_timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "filename": frame.filename,
            "lineno": frame.lineno,
            "function": frame.function,
            "code_context": str(frame.code_context).strip() if frame.code_context else None,
            "index": frame.index
        })
    
    try:
        # Verifique o caminho absoluto do arquivo
        log_file_path = os.path.abspath("log.json")
        with open(log_file_path, "a") as file:
            file.write(json.dumps(log, indent=4))
        print(f"Log gravado em: {log_file_path}")
    except Exception as e:
        print(f"Erro ao escrever no arquivo de log: {e}")
        
    df = pd.DataFrame(log)
    
    print(df)
      
start()
