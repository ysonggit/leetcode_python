class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        i, j = 0, n-1 
        # O(MlogN)
        while i < m and j >=0:
            if binaryMatrix.get(i, j) == 0:
                i+=1
            else:
                j-=1
        return j + 1 if j != n-1 else -1