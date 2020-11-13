class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_t = ""
        for i in range(4):
            for j in range(0, 4):
                for k in range(0, 4):
                    if i ==j or i==k or j==k:
                        continue
                    hh = str(arr[i])+str(arr[j])
                    if hh > "23":
                        continue
                    mm = str(arr[k])+str(arr[6-i-j-k]) # 0 + 1 + 2 + 3 = 6
                    if mm > "59":
                        continue
                    if not max_t or (max_t[0:2] < hh or (max_t[0:2] == hh and max_t[3:] < mm)):
                        max_t = hh+":"+mm
        return max_t
