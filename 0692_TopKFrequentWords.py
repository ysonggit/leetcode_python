class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        freq = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(freq)
        return [heapq.heappop(freq)[1] for _ in range(k)]