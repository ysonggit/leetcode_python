class Solution:
    def reformatNumber(self, number: str) -> str:
        m = re.findall(r'\d+', number)
        num = "".join(m)
        
        def recur(num):
            if len(num) <= 3:
                return num
            if len(num) == 4:
                return num[:2] + "-" + num[2:]
            return num[:3] + "-" + recur(num[3:]) 
        return recur(num)
