class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        count = 0
        while(n != 1):
            if(n&1 == 0):
                n = n>>1
            else:
                n+=1
            count+=1
        return count