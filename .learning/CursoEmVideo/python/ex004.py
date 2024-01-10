## Primitive and print
user_input = input("Please, input data: ")
user_input_type = type(user_input)

# Print mode using format
print("The primitive type is: {}".format(user_input_type))
print("There's only spaces: {}".format(user_input.isspace()))
print("Is numeric: {}".format(user_input.isnumeric()))
print("Is alphabet: {}".format(user_input.isalpha()))
print("Is alphanumeric: {}".format(user_input.isalnum()))
print("Is uppercase: {}".format(user_input.isupper()))
print("Is capitalized: {}".format(user_input.istitle()))

# Print mode using f
print(f'The primitive type is: {user_input_type}')
print(f'There`s only spaces: {user_input.isspace()}')
print(f'Is Numeric: {user_input.isnumeric()}')
print(f'Is Alphabet: {user_input.isalpha()}')
print(f'Is Alphanumeric: {user_input.isalnum()}')
print(f'Is UpperCase: {user_input.isupper()}')
print(f'Is LowerCase: {user_input.islower()}')
print(f'Is Capitalized: {user_input.istitle()}')