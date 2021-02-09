class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverseInorder(node, presum):
            if node:
                presumRightSubtree = reverseInorder(node.right, presum)
                node.val += presumRightSubtree
                return reverseInorder(node.left, node.val) if node.left else node.val
            return presum
        reverseInorder(root, 0)
        return root
