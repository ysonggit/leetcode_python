class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # save the index of the bar from left until we get two successive numbers in descending order
        # [2, 1, 5, 6, 2, 3]
        #  s      h  area
        # [0]     2  0
        # [ ]     1  2
        # [1]     1  2
        # [1,2]   5  2
        # [1,2,3] 6  2
        # [1,2]   2  6 
        # [1]     2  10
        # [1,4]   3  10 
        # [1,4,5] 0  10
        # [1,4]   0  10 > 3
        # [1]     0  10 > 8
        # [ ]     0  10 > 6
        maxArea = 0
        n = len(heights)
        for i in range(n+1):
            curHeight = heights[i] if i < n else 0
            while stack and curHeight < heights[stack[-1]]:
                j = stack.pop() # idx of the nearest bar whose height is higher than curHeight
                width = i if not stack else i - 1 - stack[-1]
                maxArea = max(maxArea, heights[j] * width)
            stack.append(i)
        return maxArea
