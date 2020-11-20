class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < nums[hi]:
                # search right sorted part
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[mid] > nums[hi]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # 2,3,4,1,1,1,1,1 move mid to left
                hi -= 1
        return False
