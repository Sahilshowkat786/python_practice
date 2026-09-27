class Student:
    college = "IUST"

    def __init__(self, name):
        self.name = name
        self.version=1

s = Student("Sahil")
# print(s.__dict__)

x=[1,2,3]
print(dir(x))# all about this

print(x.append.__dir__)


print(help(str))