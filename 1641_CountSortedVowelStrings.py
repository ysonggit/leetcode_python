class Solution:
    def __init__(self):
        self.vowels = "aeiou"
        self.count = 0
        
    def countVowelStrings(self, n: int) -> int:
        
        def backtrack(path, cur, n):
            if len(path) == n:
                self.count += 1
                return
            for i in range(cur, 5):
                path += self.vowels[i]
                backtrack(path, i, n)
                path = path[:-1]
            
        backtrack("", 0, n)
        return self.count
