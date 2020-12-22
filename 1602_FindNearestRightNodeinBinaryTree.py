class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            curLevel = len(queue)
            targetFound = False
            for i in range(curLevel):
                cur = queue.popleft()
                if targetFound and i < curLevel:
                    return cur
                if cur == u:
                    targetFound = True
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)  
        return None
