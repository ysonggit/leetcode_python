class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        rem = K
        num = 0
        rem_set = set()
        while rem > 0:
            num = num * 10 + 1
            rem = num%K
            if rem in rem_set:
                return -1
            else:
                rem_set.add(rem)
        return len(str(num))
