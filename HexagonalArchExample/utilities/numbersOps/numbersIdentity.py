def oddNumbers(*args):
    oddNums = []
    for number in args:
        if number % 2 != 0: oddNums.append(number)
        
    return oddNums

def pairsNumbers(*args):
    pairsNums = []
    for number in args:
        if number % 2 == 0: pairsNums.append(number)
        
    return pairsNums