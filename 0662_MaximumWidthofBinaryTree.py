class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_width = 0
        level = 1
        while queue:
            cur_level = len(queue)
            x_pos = []
            for _ in range(cur_level):
                cur, x= queue.popleft()
                x_pos.append(x)
                if cur.left:
                    queue.append((cur.left, 2*x-1))
                if cur.right:
                    queue.append((cur.right, 2*x))
            max_width = max(max(x_pos) - min(x_pos)+1, max_width)
            #print("level {}, width {}".format(level, max(x_pos) - min(x_pos)+1))
            level += 1
        return max_width
