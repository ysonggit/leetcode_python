class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val, root.val)] # save tuple of node, curmin, curmax
        maxdiff = 0
        while stack:
            cur, curmin, curmax = stack.pop()
            if cur.left:
                stack.append((cur.left, min(cur.left.val, curmin), max(cur.left.val, curmax)))
            if cur.right:
                stack.append((cur.right, min(cur.right.val, curmin), max(cur.right.val, curmax)))
            if not cur.left and not cur.right: # only find diff when reaching a leaf node
                maxdiff = max(maxdiff, abs(curmax - curmin))
        return maxdiff
