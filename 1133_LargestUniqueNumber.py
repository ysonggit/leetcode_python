class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        occurOneMax = -1
        for k, v in freq.items():
            if v == 1:
                # all inputs are positives
                if occurOneMax < k:
                    occurOneMax = k
        return occurOneMax
