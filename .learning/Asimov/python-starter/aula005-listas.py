# Gerando uma lista de 0-10
# Adicionando um valor a cada interação na lista, como um dicionário

list =[]
list2 =[]
list3 =[]

for i in range(0,5):
    list = list + [i]
    
for i in range(6,11):
    list2 = list2 + [i]
    
for i in range(12,20):
    list3 = list3 + [i]


# Ultimo elemento da lista
list[-1:]
# Primeiro elemento da lista
list[0:1]
# Adicionando um novo valor na lista com append
list.append("Um novo valor")
# remove por padrão o último valor da lista
list.pop() # equivalente a pop(-1)
# removendo o primeiro valor da lista gerada
list.pop(1)
# Ordernando uma lista
list.sort()
# Invertendo uma lista
list = ["a","b","c","d"]
list.reverse()
## Trabalhando com mais de uma lista
# Adicionando outras listas dentro de uma lista nova
list_final = [list, list2, list3]
# adicionando valores de outras dentro de uma lista novalist_final = [list, list2, list3]
numbers = [list + list2 +  list3]


minha_lista = [1, 2, 3, 4, 3, [1, 2, 3]]

minha_lista[4:]



