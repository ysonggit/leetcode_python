class Solution:
    def checkValidString(self, s: str) -> bool:
        min_cnt = max_cnt = 0 # min/max count of )
        if len(s) == 0:
            return True
        for c in s:
            if c == '(':
                min_cnt += 1 # ()( needs min 1 ) to be valid
                max_cnt += 1 
            elif c == ')':
                max_cnt -=1 
                min_cnt = max(min_cnt-1, 0) # "*)" 
            else:
                max_cnt += 1 # *
                min_cnt = max(min_cnt-1, 0) # (* is valid
            if max_cnt < 0:
                return False
        return min_cnt == 0