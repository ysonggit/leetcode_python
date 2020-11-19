class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(1, beginWord)])
        while queue:
            dist, cur = queue.popleft()
            if cur == endWord:
                return dist
            for i in range(len(cur)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nex = cur[:i]+c+cur[i+1:]
                    if nex in wordList:
                        queue.append((dist+1, nex))
                        wordList.remove(nex)
        return 0
