class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 :
            return 0
        nums = [0] * (n+1)
        nums[1] = 1
        for j in range(2, n+1):
            if j % 2 ==0:
                nums[j] = nums[j//2]
            else:
                # 2 * i + 1 = j
                nums[j] = nums[(j-1)//2] +nums[(j+1)//2]
        return max(nums)
                
