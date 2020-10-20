class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        
        newnode = Node(node.val)
        self.visited[node] = newnode
        for nb in node.neighbors:
            newnode.neighbors.append(self.cloneGraph(nb))
            
        return newnode