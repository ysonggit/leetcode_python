class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.stack = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.stack:
            self.stack.append(self.iter.next())
        return self.stack[-1]
            
    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0 or self.iter.hasNext()
