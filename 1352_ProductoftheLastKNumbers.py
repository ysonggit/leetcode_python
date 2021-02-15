class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]
        else:
            self.prefixProduct.append(self.prefixProduct[-1]* num)

    def getProduct(self, k: int) -> int:
        #  [3,2,5,4]
        # 1 3 6 30 120
        #  [3,0,2,5,4]
        # 1 3 0,2,10 40
        # check if 0 in prefixProduct[-k:]
        if k >= len(self.prefixProduct):
            return 0
        return self.prefixProduct[-1]//self.prefixProduct[-k-1]
