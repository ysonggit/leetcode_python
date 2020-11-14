class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copied = {}
        
        def deepcopy(cur):
            if not cur:
                return None
            if cur in copied:
                return copied[cur]
            copied[cur] = Node(cur.val)
            copied[cur].next = deepcopy(cur.next)
            copied[cur].random = deepcopy(cur.random)
            return copied[cur]
            
        return deepcopy(head)
