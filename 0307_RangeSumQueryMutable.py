class NumArray:
    '''
    https://www.youtube.com/watch?v=uSFzHCZ4E-8
    '''
    def __init__(self, nums: List[int]):
        self.BIT = [0] * (len(nums)+1)
        self.nums = nums
        for i in range(len(nums)):
            self.updateBIT(i, nums[i])
        #print(self.BIT)
        
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        self.updateBIT(i, diff)

    def updateBIT(self, i: int, val: int) -> None:
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & (-i)
            
    def sumRange(self, i: int, j: int) -> int:
        return self.prefixSum(j) - self.prefixSum(i-1)
        
    def prefixSum(self, i: int) -> int:
        res = 0
        i += 1
        while i > 0:
            res += self.BIT[i]
            i -= i & (-i) # flip the last set bit
        return res
