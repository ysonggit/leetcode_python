from threading import Condition
class DiningPhilosophers:
    
    def __init__(self):
        self.c = Condition()
        self.free = [True for _ in range(5)]
    
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        i = philosopher
        with self.c:
            while not self.free[i] or not self.free[(i+1)%5]:
                self.c.wait()
            self.free[i], self.free[(i+1)%5] = False, False
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        with self.c:
            while self.free[i] or self.free[(i+1)%5]:
                self.c.wait()
            self.free[i], self.free[(i+1)%5] = True, True
            self.c.notify() 

