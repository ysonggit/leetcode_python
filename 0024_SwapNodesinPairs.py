class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode('-1')
        dummy.next = head
        pre, cur = dummy, dummy.next
        while pre and cur and cur.next:
            # pre --> cur --> nex --> nex2
            nex = cur.next
            nex2 = cur.next.next
            pre.next = nex
            nex.next = cur
            cur.next = nex2
            # pre --> nex --> cur --> nex2
            pre = cur
            cur = nex2            
        return dummy.next
