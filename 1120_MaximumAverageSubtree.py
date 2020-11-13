class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_avg = 0
        def averageSubtree(cur):
            if not cur:
                return [0, 0]
            left_sum, left_cnt = averageSubtree(cur.left)
            right_sum, right_cnt = averageSubtree(cur.right)
            cur_sum = left_sum + right_sum + cur.val
            cur_cnt = left_cnt+right_cnt+1
            self.max_avg = max(self.max_avg, cur_sum/cur_cnt)
            return [cur_sum, cur_cnt]
        
        averageSubtree(root)
        return self.max_avg
