class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        tree = defaultdict(set)
        forward_queue = deque([beginWord])
        backward_queue = deque([endWord])
        queue = set()
        found = False
        reverse_direction = False
        res = []
        while forward_queue and not found:
            wordset -= set(forward_queue)
            for cur in forward_queue:
                for i in range(len(cur)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nex = cur[:i]+c+cur[i+1:]
                        if nex in wordset:
                            if nex in backward_queue:
                                found = True
                            else:
                                queue.add(nex)
                            if reverse_direction:
                                tree[nex].add(cur)
                            else:
                                tree[cur].add(nex)
            forward_queue, queue = queue, set()
            if len(forward_queue) > len(backward_queue):
                forward_queue, backward_queue, reverse_direction = backward_queue, forward_queue, not reverse_direction
       
        def backtrack(x):
            return [[x]] if x==endWord else [[x] + rest for y in tree[x] for rest in backtrack(y)]
        return backtrack(beginWord)
