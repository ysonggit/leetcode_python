class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        queue = []
        queue.append(root)
        orphans = []
        while len(queue) > 0:
            cur = queue[0]
            queue.pop(0)
            if cur.left != None and cur.right == None:
                orphans.append(cur.left.val)
            if cur.left == None and cur.right != None:
                orphans.append(cur.right.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return orphans