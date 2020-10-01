class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent