class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode('d')
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        h1 = dummy.next
        l, r = self.sortList(h1), self.sortList(h2)
        return self.mergeList(l, r)
        
    def mergeList(self, h1: ListNode, h2: ListNode) -> ListNode:
        if not h1 or not h2:
            return h1 or h2
        dummy = ListNode('d')
        tail = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next

        tail.next = h1 or h2
        return dummy.next