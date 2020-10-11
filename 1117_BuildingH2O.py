from threading import Semaphore
class H2O:
    def __init__(self):
        self.h, self.o = Semaphore(1), Semaphore(0)
        self.h_cnt = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_cnt += 1
        if self.h_cnt == 2:
            self.h_cnt = 0
            self.o.release()
        else:
            self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h.release()