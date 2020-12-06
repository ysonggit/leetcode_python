class Solution:
    def connect(self, root: 'Node') -> 'Node':  
        def dfs(cur, parent):
            if not cur:
                return          
            if parent and cur == parent.left:
                if parent.right:
                    cur.next = parent.right
                else:
                    cur.next = nearestCousin(parent.next)
            if parent and cur== parent.right:
                cur.next = nearestCousin(parent.next)   
            # must do right subtree first
            dfs(cur.right, cur)
            dfs(cur.left, cur)
    
        def nearestCousin(parent):
            if not parent:
                return None
            return parent.left or parent.right or nearestCousin(parent.next)   
        
        dfs(root, None)
        return root
