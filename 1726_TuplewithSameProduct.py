class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = defaultdict(int)
        n = len(nums)
        res = 0
        '''
        1. (a,b) => can be arranged in 2! way => (a,b) or (b,a)
        2. (c,d) => can be arranged in 2! way => (c,d) or (d,c)
        3. Consider X = (a,b) and Y = (c,d) => In how many way (X,Y) can be arranged => 2! way => (X,Y) or (Y,X)
        '''
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                res += 8 * prods[a*b]
                prods[a*b] += 1
        return res
