class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        sumCnts = defaultdict(int)
        prefixSum = 0
        res = 0
        sumCnts[0] = 1
        #          [1,2,3] 3
        #         0  1  3  6
        # sumCnts 1  1  1  1
        for i in nums:
            prefixSum += i
            if prefixSum - k in sumCnts:
                res += sumCnts[prefixSum-k]
            sumCnts[prefixSum] += 1
        return res
