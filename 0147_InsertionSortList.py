class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode('#')
        dummy.next = head
        cur = dummy.next
        # 4->2->1->3
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                to_insert = cur.next    # 2
                cur.next = cur.next.next# 4 -> 1 
                pre = dummy            
                while pre.next and pre.next.val < to_insert.val:
                    pre = pre.next
                to_insert.next = pre.next # 2 -> 4
                pre.next = to_insert      
        return dummy.next
