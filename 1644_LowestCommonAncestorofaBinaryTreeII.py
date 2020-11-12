class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        # post order traversal
        # if cur node matches p or q, return True, otherwise, False
        def findLCA(cur, p, q):
            if not cur:
                return False
            is_left_ancestor = findLCA(cur.left, p, q)
            is_right_ancestor = findLCA(cur.right, p, q)
            if (is_left_ancestor or is_right_ancestor) and (cur == p or cur==q):
                self.lca = cur
                return False
            if is_left_ancestor and is_right_ancestor:
                self.lca = cur
                return False
            if cur == p:
                return True
            if cur == q:
                return True
            return is_left_ancestor or is_right_ancestor
        findLCA(root, p, q)
        return self.lca
