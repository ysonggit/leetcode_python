class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def findLca(root, p, q):
            if not root:
                return None
            if root.val == q or root.val == p:
                return root
            left_ancestor = findLca(root.left, p, q)
            right_ancestor = findLca(root.right, p, q)
            if left_ancestor and right_ancestor:
                return root
            return left_ancestor or right_ancestor
        lca = findLca(root, p, q)
        #print(lca.val)
        dist = 0
        queue = deque([(0, lca)])
        while queue:
            size = len(queue)
            for _ in range(size):
                depth, cur = queue.popleft()
                if cur.val in [p, q]:
                    dist += depth
                if cur.left:
                    queue.append((depth+1, cur.left))
                if cur.right:
                    queue.append((depth+1, cur.right))
        return dist
