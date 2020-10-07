class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        target, cur_sum, parts = total//3, 0, 0
        for i in A:
            cur_sum += i
            if cur_sum == target:
                cur_sum = 0
                parts+=1
        return parts == 3 or (target==0 and parts > 3)