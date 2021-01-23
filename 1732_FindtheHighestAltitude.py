class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefixSum = [0]*(n+1)
        for i in range(1, n+1):
            prefixSum[i] = prefixSum[i-1] + gain[i-1]
        return max(prefixSum)
