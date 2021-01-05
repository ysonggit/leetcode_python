class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(int)
        for x in arr:
            freq[x] += 1
        sorted_freq = {num: v for num, v in sorted(freq.items(), key=lambda x: x[1])}
        # greedy
        for num, v in sorted_freq.items():
            if k >= v:
                k -= v
                sorted_freq[num] = 0
            elif 0 < k < v:
                k = 0
                sorted_freq[num] = v - k
                break
            else:
                break
        res = 0
        for num, v in sorted_freq.items():
            #print(num, v)
            if v > 0:
                res += 1
        return res
