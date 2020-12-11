class BSTIterator:

    def __init__(self, root: TreeNode):
        def inorder(cur):
            return inorder(cur.left) + [cur.val] + inorder(cur.right) if cur else []
        self.arr = inorder(root)
        self.n = len(self.arr)
        self.cur = -1
        
    def hasNext(self) -> bool:
        return self.cur < self.n - 1

    def next(self) -> int:
        self.cur += 1
        return self.arr[self.cur]
    
    def hasPrev(self) -> bool:
        return self.cur > 0
        
    def prev(self) -> int:
        self.cur -= 1
        return self.arr[self.cur]
