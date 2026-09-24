class Animal:
    def __init__(self,name,age,color):
        self._name=name
        self._age=age
        self._color=color
    def intro(self):
        print(f"My pets name is {self._name} and age is {self._age} and color is {self._color}")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,val):
        self._name=val
    

a=Animal("dog",12,"Black")
a.intro()
a.name="Cat"
print(a.name)

