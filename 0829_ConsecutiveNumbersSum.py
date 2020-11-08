class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # a + a + 1 + a + 2 ... + a + k = N
        # a*(k+1) + sum(1...k) = a*(k+1) + k*(k+1)/2 = N
        # a = (N - (k+1)*k/2)/(k+1) = N/(k+1) - k/2 > 0
        # N > (k+1)k/2
        # if a is integer then a - floor(N/(k+1) - k/2) == 0
        cnt = 0
        k = 0
        while (k/2)*(k+1) < N:
            a = N/(k+1) - k/2;
            if a - math.floor(a) == 0:
                cnt += 1
            k += 1
        return cnt
