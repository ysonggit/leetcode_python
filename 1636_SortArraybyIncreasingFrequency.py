class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))
