class Shape:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
class Circle(Shape):
    def __init__(self,a):
         self.a=a
         super().__init__(a,a)
    def area(self):
         return 3.14 * self.a * self.a
         
# rec=Shape(3,5)
# rec.area()
cir=Circle(3)
print(cir.area())