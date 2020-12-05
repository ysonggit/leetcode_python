class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        m = len(flowerbed)
        for i in range(1, m+1):
            if bed[i] == 0 and bed[i-1] == 0 and bed[i+1] == 0:
                bed[i] = 1
                n -= 1
        return n <= 0 
