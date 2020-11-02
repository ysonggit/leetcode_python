class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0, 0)])
        vals = []
        while queue:
            num = len(queue)
            for _ in range(num):
                cur, x, y = queue.popleft()
                vals.append([cur.val, x, y])
                if cur.left:
                    queue.append((cur.left, x+1, y-1))
                if cur.right:
                    queue.append((cur.right, x+1, y+1))
        res = []
        vals.sort(key=lambda t: (t[2], t[1]))
        pos_group = defaultdict(list)
        for val, _, y in vals:
            pos_group[y].append(val)
        for k in pos_group:
            res.append(pos_group[k])
        return res
