class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # lever order / BFS but from right to left
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i == 0:
                    res.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return res
