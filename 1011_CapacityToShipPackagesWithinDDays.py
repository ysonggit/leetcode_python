class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low, high = max(weights), sum(weights)
        # binary search capacity between [low, high]
        while low < high:
            mid = (low + high)//2
            days = 1
            loads = 0
            for w in weights:
                if loads + w > mid:
                    days += 1
                    loads = 0
                loads += w
            if days > D:
                low = mid + 1
            else:
                high = mid
        return low
