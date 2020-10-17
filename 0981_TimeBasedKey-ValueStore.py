class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        all_vals = self.d[key]
        lo, hi = 0, len(all_vals)-1
        while lo < hi:
            mid = (hi+lo+1)//2
            if all_vals[mid][1] > timestamp:
                hi = mid-1
            else:
                lo = mid
        return all_vals[lo][0] if all_vals[lo][1] <= timestamp else ""