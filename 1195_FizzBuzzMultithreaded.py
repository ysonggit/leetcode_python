from threading import Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.flock, self.block, self.fblock, self.plock = Semaphore(0), Semaphore(0), Semaphore(0), Semaphore(1)
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	for i in range(self.n // 3 - self.n // 15):
            self.flock.acquire()
            printFizz()
            self.plock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	for i in range(self.n // 5 - self.n // 15):
            self.block.acquire()
            printBuzz()
            self.plock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 15):
            self.fblock.acquire()
            printFizzBuzz()
            self.plock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.plock.acquire()
            if i % 15 == 0:
                self.fblock.release()
            elif i % 3 == 0:
                self.flock.release()
            elif i % 5 ==0:
                self.block.release()
            else:
                printNumber(i)
                self.plock.release()