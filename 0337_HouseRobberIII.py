class Solution:
    def rob(self, root: TreeNode) -> int:
        
        @functools.lru_cache(None)
        def dfs(node, parent_robbed=False):
            if not node:
                return 0
            # don't rob current
            if not parent_robbed:
                rob_cur = node.val + dfs(node.left, True) + dfs(node.right, True)
                no_rob = dfs(node.left, False) + dfs(node.right, False)
                return max(rob_cur, no_rob)
            return dfs(node.left, False) + dfs(node.right, False)
        return dfs(root)
