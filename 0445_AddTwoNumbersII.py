class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addNodes(n1, n2, carry):
            v1 = 0 if not n1 else n1.val
            v2 = 0 if not n2 else n2.val
            pre = ListNode((v1+v2+carry)%10)
            carry = (v1+v2+carry)//10
            return pre, carry        
        s1, s2 = [], []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        dummy = ListNode('#')
        carry = 0
        while s1 and s2:
            cur = dummy.next
            pre, carry = addNodes(s1.pop(), s2.pop(), carry)
            pre.next = cur
            dummy.next = pre
        remain = s1 or s2
        while remain:
            cur = dummy.next
            pre, carry = addNodes(remain.pop(), None, carry)
            pre.next = cur
            dummy.next = pre
        if carry == 1:
            cur = dummy.next
            pre = ListNode(carry)
            pre.next = cur
            dummy.next = pre
            
        return dummy.next
