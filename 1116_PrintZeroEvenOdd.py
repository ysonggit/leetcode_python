from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z, self.e, self.o = Lock(), Lock(), Lock()
        self.e.acquire()
        self.o.acquire()
        self.toprint = 1 
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.z.acquire()
            printNumber(0)
            if self.toprint % 2 == 0:
                self.e.release()
            else:
                self.o.release()
            
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n//2):
            self.e.acquire()
            printNumber(self.toprint)
            self.toprint += 1
            self.z.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n+1)//2):
            self.o.acquire()
            printNumber(self.toprint)
            self.toprint += 1
            self.z.release()