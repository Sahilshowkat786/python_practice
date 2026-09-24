class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetail(self):
        print(f"The name of Employee {self.id} is {self.name}")
#inheritance
class Programmer(Employee):
    def showLang(self):
        print("The default Language is Python ")
class Tester(Programmer):
    def Mywork(self):
        print("Tester is better than coder ")
e1=Tester("Syed",789)
e1.showDetail()
e1.showLang()
e1.Mywork()