class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        num_a, num_b, num_c = 0, 0, 0 # number of continuous a, b, c
        res = ""
        total = a + b + c
        while total > 0:
            # append a when a is the largest and num_a < 2 OR num_b or num_c == 2 and a > 0
            if (a >= b and a >= c and num_a < 2) or (a > 0 and (num_b == 2 or num_c == 2)):
                res += "a"
                num_a += 1
                a -= 1
                num_b, num_c = 0, 0
            # append b 
            elif (b >=a and b >=c and num_b < 2) or (b> 0 and (num_a==2 or num_c == 2)):
                res += "b"
                num_b += 1
                b -= 1
                num_a, num_c = 0, 0
            # append c
            elif (c >= b and c>=a and num_c < 2) or (c>0 and (num_b == 2 or num_a == 2)):
                res += "c"
                num_c += 1
                c -= 1
                num_a, num_b = 0, 0
            total -= 1
        return res
