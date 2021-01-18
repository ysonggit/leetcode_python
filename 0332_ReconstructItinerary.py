class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in tickets:
            graph[f].append(t)
        for k in graph:
            graph[k].sort(reverse=True)
        # [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        # JFK - NRT KUL
        # NRT - JFK
        visited = ["JFK"]
        routes = []
        while visited:
            top = visited[-1]
            #print("stack/visited: ", visited)
            if top in graph and len(graph[top]) > 0:
                visited.append(graph[top].pop())
            else:
                # add to routes because this is the last stop of an iternery
                #print("last stop:", visited[-1])
                routes.append(visited.pop())
                #print(routes)
        return routes[::-1]
