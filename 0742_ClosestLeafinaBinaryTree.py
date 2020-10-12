class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = defaultdict(list)
        leaves = set()
        # BFS with queue: search the shortest path to leaf
        queue = deque()
        visited = set()
        
        # DFS recursively: construct graph and collecting leaf nodes
        def dfs(node: TreeNode,  parent: TreeNode):
            if node:
                if node.val == k:
                    queue.append(node)
                if not node.left and not node.right:
                    leaves.add(node.val)
                if parent:
                    graph[node].append(parent)
                    graph[parent].append(node)
                if node.left:
                    dfs(node.left, node)
                if node.right:
                    dfs(node.right, node)
        
        dfs(root, None)

        while len(queue) > 0:
            cur_level = len(queue)
            for _ in range(cur_level):
                cur = queue.popleft()
                if cur.val in leaves:
                    return cur.val
                visited.add(cur)
                for nb in graph[cur]:
                    if nb not in visited:
                        queue.append(nb)
        return root.val