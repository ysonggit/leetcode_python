class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        cur = root
        while len(stack) > 0 or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()               
                if cur.val > p.val:
                    return cur
                cur = cur.right
        return None