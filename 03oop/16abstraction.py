from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog braks: woof")
class Cow(Animal):
    def sound(self):
        print("cow sounds like : haaw")


d=Dog()
d.sound()

    


