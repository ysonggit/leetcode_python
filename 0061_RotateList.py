class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = self.getLength(head)
        if n == 0:
            return None
        steps = n - k%n
        cur = head
        while cur.next != None:
            cur = cur.next
        cur.next = head
        for _ in range(steps):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        return newhead
        
    def getLength(self, head: ListNode) -> int:
        n = 0
        while head != None:
            head = head.next
            n+=1
        return n