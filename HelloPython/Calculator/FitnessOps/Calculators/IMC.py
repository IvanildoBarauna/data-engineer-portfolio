def CALC(weight, height):
    ## print("LOG: input_data: weight= {} height= {} ".format(weight,height))
    print(f"LOG: input_data: weight={weight} height={height}")

    # try:
    #     weight = float(weight)
    #     height = float(height)
    # except ValueError:
    #     print('ERR: Impossible imc calc. values[{}-{}]'.format(weight,height))
    #     quit()

    print("LOG: ###### RESULTS ######")
    if height != 0:
        imc_result = weight / (height * height)
        imc_result = round(imc_result, 2)
        print("YOUR IMC RESULT IS: {}".format(imc_result))
        print("LOG: ###### RESULTS ######")
    else:
        print(
            "ERR: The second value is zero. This division {} / {} isn't possible.".format(
                weight, height
            )
        )
