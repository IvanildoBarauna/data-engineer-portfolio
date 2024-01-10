"""
Este programa está sendo desenvolvido em parceria com a ASIMOV academy
"""
import pandas as pd

file_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/python/src/__databases/youtubers_df.csv"

## Carregar os dados para um objeto dataframe
df = pd.read_csv(file_path)

## Mostrar um número n de linhas
df.head(10)
## Mostrar as columnas do dataframe
df.columns

## Analise de Colunas

total_youtubers = df["Username"].count()
soma_likes = df["Likes"].sum()

print(f'O TOTAL DE YOUTUBERS ANALISADOS FOI: {total_youtubers}')
print(f'ELES TIVERAM UM TOTAL DE: {soma_likes}')
print(f'A QUANTIDADE MÉDIA DE LIKES POR YOUTUBERS FOI DE: {soma_likes / total_youtubers}')

## Mostrando apenas números ímpares


for i in range(0,10 + 1):
    if i % 2 == 0:
        print(f'Par Number: {i}')
