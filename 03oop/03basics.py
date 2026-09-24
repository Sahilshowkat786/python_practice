class Cars:
    def __init__(self,speed):
        self._speed =speed
    #getter
    @property
    def speed(self):
        return self._speed

    #setter
    @speed.setter
    def speed(self,val):
        self._speed=val

c=Cars(10)
print(c.speed)
c.speed=200
print(c.speed)




class Cars:

    def __init__(self, speed):
        self._speed = speed

    # Getter
    @property
    def speed(self):
        return self._speed

    # Setter
    @speed.setter
    def speed(self, val):
        self._speed = val


c = Cars(10)

print(c.speed)     # Getter

c.speed = 50       # Setter

print(c.speed)     # Getter