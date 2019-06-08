from abc import *

class A(metaclass=ABCMeta):
    @abstractmethod
    def process1(self):
        pass

class B(metaclass=ABCMeta):
    @abstractmethod
    def process2(self):
        pass

class C(metaclass=ABCMeta):
    @abstractmethod
    def process3(self):
        pass

class D(A, B, C):
    def process1(self):
        print("1")
    def process2(self):
        print("2")
    def process3(self):
        print("3")


d = D()
d.process1()
d.process2()
d.process3()