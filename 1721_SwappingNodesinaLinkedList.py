class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy.next
        a = None
        i = 1
        while cur:
            if i == k:
                a = cur
                break
            cur = cur.next
            i += 1        
        i = 0
        b = dummy.next
        c = dummy.next
        while c and i < k:
            c = c.next
            i += 1   
        while c:
            b = b.next
            c = c.next
        # swap a and b
        a.val, b.val = b.val, a.val
        return dummy.next
