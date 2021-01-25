class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre1, cur1 = -1, -1
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                if pre1 == -1:
                    pre1 = i
                elif pre1 > -1 and cur1 == -1:
                    cur1 = i
                    if cur1 - pre1 - 1 < k:
                        return False
                elif pre1 > -1 and cur1 > -1:
                    pre1 = cur1
                    cur1 = i
                    if cur1 - pre1 - 1 < k:
                        return False
            i += 1
        return True
