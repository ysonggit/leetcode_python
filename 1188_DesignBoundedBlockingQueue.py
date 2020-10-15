from threading import Condition
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.n = capacity
        self.c = Condition()
        self.nums = deque([])
        
    def enqueue(self, element: int) -> None:
        with self.c:
            while len(self.nums) == self.n:
                self.c.wait()
            self.nums.append(element)
            self.c.notify()
            
    def dequeue(self) -> int:
        res = -1
        with self.c:
            while len(self.nums) == 0:
                self.c.wait()
            res = self.nums.popleft()
            self.c.notify()
        return res
    
    def size(self) -> int:
        return len(self.nums)    


from threading import Semaphore
class BoundedBlockingQueue1(object):

    def __init__(self, capacity: int):
        self.n = capacity
        self.e = Semaphore(self.n)
        self.d = Semaphore(0)
        self.nums = deque([])
        
    def enqueue(self, element: int) -> None:
        self.e.acquire()
        self.nums.append(element)
        self.d.release()
            
    def dequeue(self) -> int:
        res = 0
        self.d.acquire()
        res = self.nums.popleft()
        self.e.release()
        return res
    
    def size(self) -> int:
        return len(self.nums)  