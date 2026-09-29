#magic method /dunder
class emp:
    name = "sahil"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
e = emp()

# print(e.name)
# print(len(e))

class Person:
    def __str__(self):
        return f"Yes, i am str method called when obj is calls me"
    def __call__(self,a,b):
        return a+b
s=Person()
# print(s)
sum=s()
print



