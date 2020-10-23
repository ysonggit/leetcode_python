class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        lo, hi = 0, 1
        while reader.get(hi) < target:
            lo, hi = hi, hi << 1
        while lo <= hi:
            mid = (lo + hi) //2
            val = reader.get(mid)
            if val == target:
                return mid
            else:
                if val > target:
                    hi = mid -1
                else:
                    lo = mid + 1
        return -1