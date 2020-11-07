class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 2 SUM Store the remainders in the hashmap and check if the current number has remaining remainder available in the hashset 
        if len(arr)%2==1:
            return False
        cache = defaultdict(int)
        count = 0
        for x in arr:
            remainder = k - (x % k)
            if remainder in cache and cache[remainder] >= 1:
                count += 1
                cache[remainder] -= 1
            else:
                cache[(x%k) or k] += 1
            '''
            print(x)
            print(remainder)
            print(cache)
            print('---------------------')
            '''
        return count == len(arr)//2
