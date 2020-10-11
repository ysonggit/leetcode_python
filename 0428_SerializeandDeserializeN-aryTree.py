class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def tuplify(root):
            return root and (root.val, [tuplify(c) for c in root.children])
        return json.dumps(tuplify(root))
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def detuplify(t):
            if t:
                root = Node(t[0], [])
                for c in t[1]:
                    root.children.append(detuplify(c))
                return root
            return None
        return detuplify(json.loads(data))