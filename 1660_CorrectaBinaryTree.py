class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.right:
                if cur.right.right in queue:
                    cur.right = None
                else:
                    queue.append(cur.right)
            if cur.left:
                if cur.left.right in queue:
                    cur.left = None
                else:
                    queue.append(cur.left)
            
        return root
