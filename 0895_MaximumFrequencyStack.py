class FreqStack:

    def __init__(self):
        self.freqNums = defaultdict(list)
        self.maxFreq = 0
        self.numFreq = defaultdict(int)

    def push(self, x: int) -> None:
        self.numFreq[x] += 1
        self.freqNums[self.numFreq[x]].append(x)
        self.maxFreq = max(self.maxFreq, self.numFreq[x])

    def pop(self) -> int:
        res = self.freqNums[self.maxFreq].pop()
        #self.maxFreq = max(self.freq.values())
        if len(self.freqNums[self.maxFreq])==0:
            self.maxFreq -= 1
        self.numFreq[res] -= 1
        return res
