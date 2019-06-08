from abc import *

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def howl(self):
        pass


class Dog(Animal):
    def gorogor(self):
        print("ごろごろ")

    def howl(self):
        print("BOWBOW")

myPet = Dog()
myPet.howl()