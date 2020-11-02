class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.vals = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.pos[val] = len(self.vals) 
            self.vals.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        tailidx = len(self.vals) - 1
        tailval = self.vals[tailidx] 
        idx = self.pos[val]
        self.vals[idx] = tailval
        self.pos[tailval] = idx
        self.pos.pop(val)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice( self.vals )
