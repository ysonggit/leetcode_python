from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockfoo, self.lockbar = Lock(), Lock()
        self.lockbar.acquire()
        
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockfoo.acquire()
            printFoo()
            self.lockbar.release()
            

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockbar.acquire()
            printBar()
            self.lockfoo.release()