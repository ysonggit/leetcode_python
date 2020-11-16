class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        h = [(head.val, i) for i, head in enumerate(lists) if head]
        heapq.heapify(h)
        dummy = ListNode('#')
        cur = dummy
        while h:
            idx = heapq.heappop(h)[1]
            head = lists[idx]
            if head:
                head_sub = head.next
                cur.next = head
                cur = cur.next
                if head_sub:
                    lists[idx] = head_sub
                    heapq.heappush(h, (head_sub.val, idx))
        return dummy.next
