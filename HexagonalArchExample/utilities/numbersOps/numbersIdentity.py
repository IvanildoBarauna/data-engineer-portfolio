class NumbersParity:
    
    def __init__(self, *args) -> None:
        self.nums = args,
        self.odds = self.NumbersParity()[0],
        self.pairs = self.NumbersParity()[1],
        

    def NumbersParity(self):
        """
        Input: Any numbers
        Output: Two lists, the first is Pairs Numbers and second odd Numbers
        """
        oddNums = []
        pairsNums = []
        
        for number in self.nums:
            if number % 2 == 0:
                pairsNums.append(number)
            elif number % 2 != 0:
                oddNums.append(number)
            
        return pairsNums, oddNums