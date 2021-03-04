class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(head):
            res = 0
            cur = head
            while cur:
                res += 1
                cur = cur.next
            return res
        
        lenA, lenB = getLength(headA), getLength(headB)
        d = abs(lenB-lenA)
        if lenB > lenA:
            for _ in range(d):
                headB = headB.next
        if lenA > lenB:
            for _ in range(d):
                headA = headA.next
        for _ in range(min(lenA, lenB)):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
