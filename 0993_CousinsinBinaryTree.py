class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False
        queue = deque([(root, None, 0)]) # tuple of (node, parent, depth)
        xy = [] # tuple of (parent, depth)
        while len(queue) > 0:
            level_size = len(queue)
            cur, parent, depth = queue.popleft()
            if cur.left != None:
                queue.append((cur.left, cur, depth+1))  
            if cur.right != None:
                queue.append((cur.right, cur, depth+1))
            if cur.val == x or cur.val == y:
                xy.append((parent, depth))
        return xy[0][0] != xy[1][0] and xy[0][1] == xy[1][1]
                     