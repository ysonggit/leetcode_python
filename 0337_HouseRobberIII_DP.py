class Solution:
    def rob(self, root: TreeNode) -> int:    
        # dp[]: dp[0] max gain by robbing current, dp[1] max gain by not robbing current
        def dfs(node):
            dp = [0, 0]
            if not node:
                return dp
            left = dfs(node.left)
            right = dfs(node.right)
            # rob current, following two descendants can NOT be robbed
            dp[0] = node.val + left[1] + right[1]
            # skip current, left and right can be choosen either robbed or not
            dp[1] = max(left[0], left[1]) + max(right[0], right[1]) 
            return dp
        return max(dfs(root))
