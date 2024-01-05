"""
MELI CHALENGER
1. Abaixo você encontrará declarações que você deve resolver, você deve ter em mente que existem dois arquivos como fontes de dados 
**Salários** e **compras**.
2. Em seguida, leia os arquivos chamados compras.csv e salários.csv
3. Importe a biblioteca do Google para fazer upload do arquivo
4. Importe cada arquivo em um dataframe diferente
1. Exiba as primeiras 5 linhas de cada DataFrame para verificar se você leu os dados corretamente.
2. De acordo com o conjunto de dados SALÁRIOS, quantos cargos eram ocupados por apenas uma pessoa em 2011? (acusações com apenas uma ocorrência em 2011):
3. De acordo com o conjunto de dados SALÁRIOS, quantas pessoas possuem a palavra 'GERENTE' em seu cargo?
4. De acordo com o conjunto de dados SALÁRIOS, qual é o nome da pessoa que ganha menos (incluindo benefícios - TotalPayBenefits)?
5) De acordo com o conjunto de dados SALÁRIOS, qual é o salário base médio (BasePay) de todos os funcionários no ano (2012)?
6) De acordo com o conjunto de dados SALÁRIOS, qual foi o valor total pago com benefícios para os dois empregos mais populares?
7) De acordo com o conjunto de dados COMPRAS, quais são os 5 provedores de e-mail mais comuns, com quantos usuários cada um está associado? (hotmail.com,gmai.com, etc)
8) De acordo com o conjunto de dados COMPRAS, quantas pessoas têm um cartão de crédito que expira em 2025?
9) De acordo com o conjunto de dados COMPRAS, quantas pessoas possuem cartões Mastercard e fizeram uma compra por mais de US$ 20?
10) De acordo com o conjunto de dados COMPRAS Alguém fez uma compra no Lote: "90 WT", qual foi o preço de compra desta transação?
11) De acordo com o conjunto de dados COMPRAS, quanto é o preço total de compra das duas empresas menos populares? Quais são essas duas empresas?
"""


import pandas as pd

compras_file_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/chalenger_meli/compras.csv"
salarios_file_path = "/Users/ivanildo_barauna/code/bitbuchet.org/bitbucket_mycodes/chalenger_meli/salarios.csv"

df_compras = pd.read_csv(compras_file_path)
df_salarios = pd.read_csv(salarios_file_path)

df_salarios.head(5)
df_compras.head(5)

# df_salarios = df_salarios.filter({"Year" == "2011" }))

df_salarios = df_salarios[df_salarios.Year.isin([2011])]

df_salarios = df_salarios.JobTitle.value_counts()

df_salarios.count()

"""
SELECT COUNT(*) FROM df_salarios 
WHERE lower(JobTitle) LIKE '%manager%';

SELECT COUNT(*) FROM df_salarios 
WHERE upper(JobTitle) LIKE '%MANAGER%';
"""

"""
WITH EMPLOYES AS (
SELECT EmployeeName, sum(TotalPayBenefits) total_pay 
FROM DF_SALARIOS 
GROUP BY EmployeeName)

SELECT * FROM EMPLOYES ORDER BY total_pay asc LIMIT 1;

WITH EMPLOYES AS (
SELECT EmployeeName, sum(TotalPayBenefits) total_pay 
FROM DF_SALARIOS 
GROUP BY EmployeeName)

SELECT * FROM EMPLOYES
WHERE TRUE QUALIFY (OVER(PARTITION BY EmployeeName ORDER BY total_pay asc ))=1
"""

"""

select avg(BasePay) from DF_SALARIOS where year = 2012 

"""

"""
DECLARE arrMostPopular array<string>;

set arrMostPopular = (select array_agg(JobTitle) from (select JobTitle, count(*) 
        from df_salarios 
        group by JobTitle order by 2 desc limit 2));

    SELECT JobTitle, sum(TotalPayBenefits) total_pay_with_benefits 
    FROM DF_SALARIOS GROUP BY JobTitle
    where jobTitle in unnest(arrMostPopular)
"""


"""
select 
    split(Email, "@")[1] provider_name
    ,
    ,count(*)
    ,count(distinct EmployeeName) total_employees
from DF_COMPRAS 
group by 1, EmployeeName
order by 2 desc
limit 5
"""
