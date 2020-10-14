class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0
        def height(node: 'Node') -> int:
            if not node:
                return 0
            max_1, max_2 = 0, 0
            for child in node.children:
                h = height(child) + 1
                if h > max_1:
                    max_2, max_1 = max_1, h
                elif h > max_2:
                    max_2 = h
            self.res = max(self.res, max_1 + max_2)
            return max_1         
        
        height(root)
        return self.res