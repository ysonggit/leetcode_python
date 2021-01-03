class Solution:
    def countArrangement(self, n: int) -> int:
        if n <= 2:
            return n
        
        self.count = 0
        def dfs(n, i, arranged, arr):
            if i > n:
                #print(arr)
                self.count += 1
                return
            for j in range(1, n+1):
                if arranged[j] == 0 and (j % i == 0 or i % j == 0):
                    arranged[j] = 1
                    arr[i-1] = j 
                    dfs(n, i+1, arranged, arr)
                    arranged[j] = 0
        arranged =[0] * (n+1)
        arr = [None] * n
        dfs(n, 1, arranged, arr)
        return self.count
