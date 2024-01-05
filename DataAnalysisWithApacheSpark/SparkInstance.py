from pyspark.sql import SparkSession
# import logging

def GetOrCreateSession() :
    
    # logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    # Verifica se a sessão Spark já existe
    
    # logging.info("Sessão Spark não existe. Criando uma nova sessão.")
    new_session = SparkSession.builder\
        .master('local')\
        .appName('spark')\
        .getOrCreate()

    return new_session