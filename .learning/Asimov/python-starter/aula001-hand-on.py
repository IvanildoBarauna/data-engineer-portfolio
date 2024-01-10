"""
Este programa está sendo desenvolvido em parceria com a ASIMOV academy
- Usar o pandas para ler um arquivo
- Mostrar dados deste arquivo 
- Mostrar as colunas deste arquivo
- Analisar uma métrica deste conjunto de dados
"""

import pandas as pd

file_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/python/src/__databases/StudentsPerformance.csv"

df = pd.read_csv(file_path)

# Etapa de Tratamento dos dados, normalizando nome de colunas
for i in range(df.shape[1]):
    old_column_name = df.columns[i]
    df = df.rename(columns={
        old_column_name: old_column_name.replace(" ", "_").replace("/", "_")
    })

# Analise de Dados
# Total de Linhas com LEN
total_rows = len(df)
# Total de Linhas com shape pegando o primeiro elemento da matriz
total_rows = df.shape[0]
# Média geral de matematica
general_math_score = df["math_score"].mean().__int__()
# Média geral de leitura
general_reading_score = df["reading_score"].mean().__int__()


avg_math_score_per_gender = df.groupby('gender')["math_score"].mean()
avg_math_score_per_race = df.groupby('race_ethnicity')["math_score"].mean()
avg_math_score_education = df.groupby('parental_level_of_education')[
    "math_score"].mean()
avg_math_score_test_preparation_course = df.groupby(
    'test_preparation_course')["math_score"].mean()

avg_reading_score_per_gender = df.groupby('gender')["reading_score"].mean()
avg_reading_score_per_race = df.groupby(
    'race_ethnicity')["reading_score"].mean()
avg_reading_score_education = df.groupby('parental_level_of_education')[
    "reading_score"].mean()
avg_reading_score_test_preparation_course = df.groupby(
    'test_preparation_course')["reading_score"].mean()

print("#" * 20)

print(f'Total Rows: {total_rows}')
print(f'General Math Score: {(general_math_score)}')
print(f'General Read Score: {(general_reading_score)}')

print("#" * 20)

print(f"""
      "Average Math Score per {avg_math_score_per_gender}" 
      
      "Average Math Score per {avg_math_score_per_race}"
      """)

print(f"Average Math Score per {avg_math_score_per_gender}")
print(f"Average Math Score per {avg_math_score_per_race}")
print(f"Average Math Score per {avg_math_score_education}")
print(f"Average Math Score per {avg_math_score_test_preparation_course}")

print(f"Average Reading Score per {avg_reading_score_per_gender}")
print(f"Average Reading Score per {avg_reading_score_per_race}")
print(f"Average Reading Score per {avg_reading_score_education}")
print(f"Average Reading Score per {avg_reading_score_test_preparation_course}")
