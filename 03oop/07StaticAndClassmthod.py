class Student:

    college = "IUST"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print(cls.college)
        #also can modify class varibles

    # Static method
    @staticmethod
    def greet():
        print("Welcome!")
    #it is a normal functio ,but associated with Class


s1 = Student("Sahil")

s1.show_name()          # self → object
Student.show_college()  # cls → class
Student.greet()         # no self/cls