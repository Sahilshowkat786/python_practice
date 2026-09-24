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
print(c._Bank__pin)

