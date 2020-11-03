class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode('#')
        dummy.next = head
        cur = dummy.next
        while cur:
            for _ in range(m-1):
                if cur:
                    cur = cur.next
                else:
                    return dummy.next
            for _ in range(n):
                if cur and cur.next:
                    cur.next = cur.next.next
                else:
                    return dummy.next
            cur = cur.next
        return dummy.next
