class StockSpanner:

    def __init__(self):
        # store prev high prices than current and accumulate the number of lower prices
        self.prev = [] 

    def next(self, price: int) -> int:
        accum = 1
        while self.prev and self.prev[-1][0] <= price:
            accum += self.prev.pop()[1]
        self.prev.append((price, accum))
        #print(self.prev)
        return accum
