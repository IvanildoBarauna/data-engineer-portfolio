def simple_math_operations(n1, n2): 
    print("########## RESULTADOS ##########")
    print("A junção dos valores resulta em :", n1 +  n2)

    try:
        n1 = int(n1)
    except ValueError: print("O primeiro valor digitado não é um número.")

    try:
        n2 = int(n2)
    except ValueError: print("O segundo valor digitado não é um número.")

    print("A soma dos números é", n1 +  n2)
    print("A multiplicação dos números é", n1 *  n2)
    if n2 != 0:
        print("A divisão dos números é", n1 /  n2)
    else:
        print("Não é possível dividir por zero")
    print("########## RESULTADOS ##########")


# v1 = input("DIGITE UM NÚMERO: ")
counter = 0
v1 = input("DIGITE UM NÚMERO: ")

while not v1:
    print("Dois números são necessários, tente novamente.", "Você possui mais" , 5 - counter, "tentativas restantes." )
    counter = counter + 1
    if counter <6:
        v1 = input("POR FAVOR, DIGITE UM NÚMERO: ")
    else:
        print("LIMITE DE TENTATIVAS EXCEDIDAS")
        break


if not v1: quit()

counter = 0
v2 = input("DIGITE OUTRO NÚMERO: ")

while not v2:
    print("Dois números são necessários, tente novamente.", "Você possui mais" , 5 - counter, "tentativas restantes." )
    counter = counter + 1
    if counter <6:
        v2 = input("POR FAVOR, DIGITE UM NÚMERO: ")
    else:
        print("LIMITE DE TENTATIVAS EXCEDIDAS")
        break
