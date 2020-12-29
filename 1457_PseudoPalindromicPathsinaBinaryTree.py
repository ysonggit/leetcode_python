class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        # return if current path pseudo palindrome
        self.res = 0
        def dfs(node, path):
            if node:
                if not node.left and not node.right:
                    # leaf node
                    # print(path + [node.val])
                    freq = Counter(path + [node.val])
                    odds = 0
                    for ele in freq:
                        if freq[ele] % 2 == 1:
                            odds += 1
                    if odds <= 1:
                        self.res += 1
                else:
                    if node.left:
                        dfs(node.left, path + [node.val])
                    if node.right:
                        dfs(node.right, path + [node.val])
        if not root:
            return 0
        dfs(root, [])
        return self.res
