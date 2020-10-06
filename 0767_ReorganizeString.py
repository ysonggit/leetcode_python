class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = collections.Counter(S) # Counter({'a': 3, 'b': 1})
        i, n = 0, len(S)
        res = [""]*n
        for char in sorted(cnt, key=cnt.get, reverse=True): # ['a','b']
            if cnt[char] > n//2 + n%2: 
                return ""
            for j in range(cnt[char]):
                #print("insert {} to {}".format(char, i%n))
                insert_idx = i%n
                if res[insert_idx] != "":
                    insert_idx+=1
                res[insert_idx] = char
                i+=2
        return "".join(res)