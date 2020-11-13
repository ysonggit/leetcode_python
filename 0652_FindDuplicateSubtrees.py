class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        self.cache = defaultdict(list) # key is serialized subtree, value is a list of subtree roots
        
        def serialize(node: TreeNode) -> str:
            if not node:
                return "#"
            res = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
            #print(res)
            self.cache[res].append(node)
            return res
        
        dup = []
        serialize(root)
        for nodes in self.cache.values():
            if len(nodes) > 1:
                dup.append(nodes[0])
        return dup
