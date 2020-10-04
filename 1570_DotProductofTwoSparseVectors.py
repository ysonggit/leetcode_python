class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = { i: v for i, v in enumerate(nums) if v != 0 }
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int: 
        prod = 0
        for i in self.nonzero:
            if i in vec.nonzero:
                prod += self.nonzero[i] * vec.nonzero[i]
        return prod
