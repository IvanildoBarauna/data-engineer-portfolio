## Multiplicando strings para exibir logs
header = "#" * 20

fisrt_name = "Ivanildo"
last_name = "Barauna de Souza Junior"
full_name = fisrt_name + ' ' + last_name

total_caracters = len(full_name)
print(f'Tamanho da string: {total_caracters}')
print(f'Concat de string: {fisrt_name} + "outra string"')

## Verticalizando uma string
for i in range(total_caracters):
    print(f'string index: {fisrt_name[i]}')



# Isso dá a possibilidade de mostrar ranges da string
# Aqui mostrando as 3 primeiras letras
fisrt_name[0:4]
# Aqui da posição 1 até a quantidade total de caracteres
fisrt_name[1:total_caracters]
# Aqui é possível usar os dois pontos para determinar a quantidade de caracteres a serem ignorados
# Retornar a string inteira porém ignorando a cada 1 caracter
full_name[::1]
# Retornar a string inteira porém ignorando a cada -1 caracter, isto é de traz pra frente
full_name[::-1]

""""
Usando os valores de forma negativa ou seja string[-1:]
é possível pegar os valores de traz pra frente, invertendo
o indice da posição, como abaixo
"""

# Calculando a posição do primeiro espaço
first_space_position = full_name.find(" ", 0)
# Calculando a posição do último espaço
last_space_position = full_name.find(" ", -total_caracters)

# Quero pegar da posição 0 da string até o primeiro espaço, ou seja
# o primeiro nome
first_name = full_name[0:first_space_position]
# Quero pegar aqui do último espaço da string até a quantidade total de caracteres
last_name = full_name[last_space_position+1:total_caracters]

voo_card = last_name.upper() + ', ' + first_name

print(header)
print(voo_card)
print(header)



