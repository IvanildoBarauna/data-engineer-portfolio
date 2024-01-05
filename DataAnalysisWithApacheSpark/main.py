from data_explorer.SparkInstance import GetOrCreateSession as SparkSession

my_spark_session = SparkSession()

df = my_spark_session.read.csv("./train.csv")

print("Essa é a quantidade de linhas do dataframe")
print(df.count())

