class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        Reservoir Sample
        """
        size = 1
        res = 0
        cur = self.head
        while cur:
            if random.random() < 1/size:
                res = cur.val
            cur = cur.next
            size += 1
        return res
