class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.cur = root

    def next(self) -> int:
        while self.cur:
            self.nodes.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.nodes.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val

    def hasNext(self) -> bool:
        return self.nodes or self.cur
