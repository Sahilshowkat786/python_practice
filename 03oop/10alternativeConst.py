class Student:
    def __init__(self,name,age):
        self.name=name
        self.age =age
    @classmethod
    def fromStr(cls,data):
        return cls(data.split("-")[0],int(data.split("-")[1]))
s1=Student("sahil",23)
print(s1.name)
data="arsalan-90"

s2=Student.fromStr(data)

print(10*(s2.age))
print(7/3)
