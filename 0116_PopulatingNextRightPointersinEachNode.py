class SolutionDFS:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node, parent):
            if not node:
                return
            if parent and node == parent.right:
                if parent.next:
                    node.next = parent.next.left
            if parent and node == parent.left:
                node.next = parent.right
            left_sub = dfs(node.left, node)
            right_sub = dfs(node.right, node)
        dfs(root, None)
        return root
       
class SolutionBFS:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level.append(cur)
            for i in range(size-1):
                level[i].next = level[i+1]
        return root
