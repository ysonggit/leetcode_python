class Solution:
    def isValidBST(self, root: TreeNode, minNode: TreeNode = None, maxNode: TreeNode = None) -> bool:
        if not root:
            return True
        if minNode and root.val <= minNode.val:
            return False
        if maxNode and root.val >= maxNode.val:
            return False
        return self.isValidBST(root.left, minNode, root) and self.isValidBST(root.right, root, maxNode)
