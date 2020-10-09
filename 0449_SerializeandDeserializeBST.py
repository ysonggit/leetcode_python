class Codec:
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(node: TreeNode, vals: List[str]):
            if node == None:
                vals.append("null")
                return
            vals.append(node.val)
            preorder(node.left, vals)
            preorder(node.right, vals)
        vals = []
        preorder(root, vals)
        return "#".join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = deque(data.split("#"))
        def constructBST(vals: List[str]) -> TreeNode:
            if len(vals) == 0:
                return None
            if vals[0] == "null":
                vals.popleft()
                return None
            root = TreeNode(int(vals.popleft()))
            root.left = constructBST(vals)
            root.right = constructBST(vals)
            return root
        return constructBST(vals)