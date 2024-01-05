def operations(n1, n2) -> str:
    print("LOG: input_data: n1= {} n2= {} ".format(n1, n2))

    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        print(
            "LOG: Impossible math operation with input_data. values[{}-{}]".format(
                n1, n2
            )
        )
        quit()

    print("LOG: ###### RESULTS ######")
    print("LOG: The sum is: ", n1 + n2)
    print("LOG: The mult is: ", n1 * n2)
    if n2 != 0:
        print("LOG: The divide is: ", n1 / n2)
    else:
        print(
            "LOG: The second value is zero. This division {} / {} isn't possible.".format(
                n1, n2
            )
        )
    print("LOG: ###### RESULTS ######")
