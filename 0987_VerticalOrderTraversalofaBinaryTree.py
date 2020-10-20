class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_pos = []
        
        def dfs(node: TreeNode, x: int, y: int):
            if not node:
                return
            node_pos.append(((x, y), node.val)) # must use nested tuple otherwise the sort by y is wrong
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        # sort node_pos by x and y 
        node_pos.sort()
        
        group_x = defaultdict(list)
        for pos, val in node_pos:
            x, _ = pos
            group_x[x].append(val)
        
        res = []
        for x in sorted(group_x):
            res.append(group_x[x])
        return res
        