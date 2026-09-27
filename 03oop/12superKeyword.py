class Parent:
    def show(self):
        print("Parent class")


class Child(Parent):
    def show(self):
        print("Child class")
        super().show()
#
c = Child()
c.show()
# super key word in constructor
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class Child(Student):
    def __init__(self,name,rollno,age):
        super().__init__(name,rollno)
        self.age=age

s=Student("sahil",18)
s2=Child("salma",15,34)
print(s2.name,s2.age)
