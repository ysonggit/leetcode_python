class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.depth = {}
        if not root:
            return None
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if left_depth == right_depth:
            return root
        if left_depth < right_depth:
            return self.subtreeWithAllDeepest(root.right)
        return self.subtreeWithAllDeepest(root.left)
        
    def maxDepth(self, node):
        if not node:
            return 0
        self.depth[node] = 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        return self.depth[node]
