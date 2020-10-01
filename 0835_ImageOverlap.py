class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        loc1, loc2, vec = [], [], defaultdict(int)
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    loc1.append((i, j))
                if img2[i][j] == 1:
                    loc2.append((i, j))
        for r1, c1 in loc1:
            for r2, c2 in loc2:
                vec[(r2-r1, c2-c1)]+= 1
        if len(vec) == 0: # [[0]],[[0]]
            return 0
        #for k, v in vec.items():
        #    print("{}:{}".format(k,v))
        return max(vec.values())