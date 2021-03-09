class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        elif d == 2:
            left, right = TreeNode(v), TreeNode(v)
            left.left = root.left
            right.right = root.right
            root.left = left
            root.right = right
            return root
        else:
            if root.left:
                self.addOneRow(root.left, v, d-1)
            if root.right:
                self.addOneRow(root.right, v, d-1)
        return root
