from SimpleMath import operations as opCalc
import datetime

print(datetime.datetime.now(), "#### LOG: STARTING ####")

total_retry = 3
retry_number = 0

n1 = input(
    "Input a number: ",
)

while not n1:
    retry_number = retry_number + 1
    if retry_number <= total_retry - 1:
        print("LOG: You have {} retry".format(total_retry - retry_number))
        input("Please, input a number: ")
    else:
        print("LOG: Limite of retry, You can try again... See You")
        break


if not n1:
    quit()

retry_number = 0
n2 = input(
    "Input a second number: ",
)

while not n2:
    retry_number = retry_number + 1
    if retry_number <= total_retry - 1:
        print("LOG: You have {} retry".format(total_retry - retry_number))
        input("Please, input a second number: ")
    else:
        print("LOG: Limite of retry, You can try again... See You")
        quit()

opCalc(n1, n2)

print(datetime.datetime.now(), "#### LOG: END ####")
