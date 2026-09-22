class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f"My name is {self.name} and i am {self.age}")
    def weWalk(self):
        print(f"I am currently walking ")

s1=Students("sahil",17)
s1.intro()
s1.weWalk()
