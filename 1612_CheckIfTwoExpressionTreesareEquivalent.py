class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        def sumTree(root: 'Node') -> str:
            if not root:
                return ""
            if root.val == "+":
                return sumTree(root.left) + sumTree(root.right)
            return root.val + sumTree(root.left) + sumTree(root.right) 
        
        return sorted(sumTree(root1)) == sorted(sumTree(root2))
