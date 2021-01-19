class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        #for k,v in graph.items():
        #    print(k, v)
        queue = deque([(0, S)])
        visited = set()
        visited.add(S)
        routes_finish = set()
        while queue:
            #print(queue)
            bus, stop = queue.popleft()
            if stop == T:
                return bus
            for i in graph[stop]:
                if i in routes_finish:
                    continue
                for nex_stop in routes[i]:
                    if nex_stop not in visited:
                        visited.add(nex_stop)
                        queue.append((bus+1, nex_stop))
                routes_finish.add(i)
        return -1
