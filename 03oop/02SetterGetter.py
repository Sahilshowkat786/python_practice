class Student:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    # Getter
    def get_age(self):
        return self._age

    # Setter
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative")


s1 = Student("Sahil", 20)

print(s1.get_age())

s1.set_age(21)

print(s1.get_age())

s1.set_age(-5)


class Student:

    def __init__(self, age):
        self._age = age

    # GETTER
    @property
    def age(self):
        return self._age

    # SETTER
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Invalid age")


s1 = Student(20)

print(s1.age)      # getter

s1.age = 21        # setter

print(s1.age)      # getter

s1.age = -5        # setter → validation