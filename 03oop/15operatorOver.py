class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i,{self.j}j,{self.k}k"
    #add of two vectors
    def __add__(self,other):
        return f"{self.i+other.i}i,{self.j + other.j}j,{self.k +other.k }k"
    #subtraction of two vectors
    def __sub__(self,other):
        return Vector(self.i-other.i , self.j - other.j , self.k -other.k)

    
    
v1=Vector(1,20,30)
v2=Vector(3,5,7)
print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(type(v1+v2))
print(type(v1-v2))