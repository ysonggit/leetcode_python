class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        multi = False
        # ["a/*Test program", "int main()", "*/b"]
        # should return ["ab"]
        for line in source:
            n = len(line)
            if not multi:
                res.append([])
            i = 0
            while i < n:
                if not multi:
                    if i < n-1 and line[i:i+2] == '//':
                        break
                    elif i < n-1 and line[i:i+2] == '/*':
                        i += 1 
                        multi = True
                    else:
                        res[-1].append(line[i])
                else:
                    if i < n-1 and line[i:i+2] == '*/':
                        i+= 1
                        multi = False
                i += 1
        return ["".join(line) for line in res if line]
