class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def revList(node):
            pre = None
            cur = node
            while cur:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            return pre
        
        rev = revList(head)
        dummy = ListNode('#')
        dummy.next = rev
        cur = dummy
        carry = 1
        while cur.next:
            val = (cur.next.val + carry) % 10 
            carry = (cur.next.val + carry)//10
            cur.next.val = val
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        dummy.next = revList(dummy.next)
        return dummy.next
