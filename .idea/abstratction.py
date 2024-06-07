from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("hello")

class Snake(Animal):
    def move(self):
        print("hi")

hmn=Human()
snk=Snake()
hmn.move()



