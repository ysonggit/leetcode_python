class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # stores the bar idx lower than current bar
        right = 0
        res = 0
        while right < len(height):
            #print(stack)
            while stack and height[right] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                    dist = right - left - 1
                    h = min(height[right], height[left]) - height[mid]
                    #print("{} * {}".format(dist, h))
                    res += h * dist
            #print("area: ", res)
            stack.append(right)
            right += 1
        return res
