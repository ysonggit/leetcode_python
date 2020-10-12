class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(node: TreeNode, parent: TreeNode):
            if node:
                if parent:
                    graph[parent].append(node)
                    graph[node].append(parent)
                if node.left:
                    dfs(node.left, node)
                if node.right:
                    dfs(node.right, node)
        dfs(root, None)
        
        queue = deque([target])
        visited = set()
        dist = 0
        res = []
        while len(queue) > 0:
            cur_level = len(queue)
            for _ in range(cur_level):
                cur = queue.popleft()
                visited.add(cur)
                if dist == K:
                    res.append(cur.val)
                for nb in graph[cur]:
                    if nb not in visited:
                        queue.append(nb)
            dist+= 1
        return res