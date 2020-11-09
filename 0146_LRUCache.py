class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        #print(self.cache)
        return v

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.cap == len(self.cache):
                #self.cache.popitem() # remove and return the LAST element # not working
                del self.cache[next(iter(self.cache))] # the 1st element is the least used
        else:
            self.cache.pop(key)
        self.cache[key] = value
