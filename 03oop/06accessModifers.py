#by default public
class Bank:
    def __init__(self,name,accountype,pin):
        self.name=name
        self.accountype=accountype
        self.pin=pin

a=Bank("sahil","saving",7765)
print(a.pin)

#protected
class Bank:
    def __init__(self,name,accountype,pin):
        self._name=name
        self._accountype=accountype
        self._pin=pin

b=Bank("sahil","saving",7765)
# print(b.pin) # can't be accessed 
print(b._name) # by this you can access

#private
class Bank:
    def __init__(self,name,accountype,pin):
        self.__name=name
        self.__accountype=accountype
        self.__pin=pin

c=Bank("sahil","saving",7765)
# print(c.pin)
# print(c._pin)
print(c._Bank__pin) #name namgling

# code from chart Gpt to learn 

# class Student:

#     def __init__(self, name, age, marks):
#         self.name = name          # Public
#         self._age = age           # Protected
#         self.__marks = marks      # Private → Name Mangling

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self._age)
#         print("Marks:", self.__marks)

# # Object
# s1 = Student("Sahil", 20, 90)

# # 1. Public
# print(s1.name)

# # 2. Protected
# print(s1._age)

# # 3. Private
# # print(s1.__marks)       # ❌ AttributeError

# # 4. Name Mangling
# print(s1._Student__marks) # ✅ Works

# # Method can access private variable
# s1.show_details()