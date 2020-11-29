class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        cur = dummy
        a_prior, b_post = None, None
        while cur.next:
            if cur.next.val == a:
                a_prior = cur
            if cur.val == b:
                b_post = cur.next
            cur = cur.next
        a_prior.next = list2
        cur = list2
        while cur:
            if cur.next == None:
                cur.next = b_post
                break
            else:
                cur = cur.next
        return dummy.next
