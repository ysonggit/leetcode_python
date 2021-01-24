class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # using a min heap of size k
        if not lists:
            return None
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                pq.append((lists[i].val, i))
        heapq.heapify(pq)
        dummy = ListNode(-1)
        cur = dummy
        while pq:
            val, idx = heapq.heappop(pq)
            head = lists[idx]
            if head:
                cur.next = head
                cur = cur.next
                if head.next:
                    lists[idx] = head.next
                    heapq.heappush(pq, (lists[idx].val, idx))  
        return dummy.next
