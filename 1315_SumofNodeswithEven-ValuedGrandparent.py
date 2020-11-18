class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def preorder(cur, parent, grandparent):
            if cur:
                if parent and grandparent:
                    if grandparent.val % 2 == 0:
                        self.total += cur.val
                    preorder(cur.left, cur, parent)
                    preorder(cur.right, cur, parent)
                else:
                    if cur.left:
                        preorder(cur.left.left, cur.left, cur)
                        preorder(cur.left.right, cur.left, cur)
                    if cur.right:
                        preorder(cur.right.left, cur.right, cur)
                        preorder(cur.right.right, cur.right, cur)
        preorder(root, None, None)
        return self.total
