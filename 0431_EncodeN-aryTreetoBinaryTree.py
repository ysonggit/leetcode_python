"""
     1
   / | \
  3  2  4
 / \
5   6

     1
    /
   3
  / \
 5   2
  \   \
   6   4
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        newroot = TreeNode(root.val)
        if root.children:
            newroot.left = self.encode(root.children[0])
        cur = newroot.left
        if cur and len(root.children) > 1:
            for i in range(1, len(root.children)):
                cur.right = self.encode(root.children[i])
                cur = cur.right
        return newroot
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        root = Node(data.val, [])
        cur = data.left
        while cur:
            root.children.append(self.decode(cur))
            cur = cur.right
        return root