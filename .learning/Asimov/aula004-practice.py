## Montar um cartão de embarque
full_name = "Ivanildo Barauna de Souza Junior"

splited_name = full_name.split()
fisrt_name = splited_name[0].capitalize()
last_name = splited_name[len(splited_name)-1]
str_voo_card = f"{last_name.upper()}, {fisrt_name}"

str_voo_card