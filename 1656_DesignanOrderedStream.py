class OrderedStream:

    def __init__(self, n: int):
        self.vals = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.vals[id-1] = value
        while self.ptr < len(self.vals) and self.vals[self.ptr]:
            self.ptr += 1
        return self.vals[id-1:self.ptr]
