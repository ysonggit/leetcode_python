class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfsSum(nlist, depth):
            dSum = 0
            for i in nlist:
                if i.isInteger():
                    dSum += depth * i.getInteger()
                else:
                    dSum += dfsSum(i.getList(), depth+1)
            return dSum
        return dfsSum(nestedList, 1)
