class Student:
    def __init__(self, name, rollno, marks):
        self.__name = name
        self.__rollno = rollno
        self.__marks = marks

    def get_student(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__rollno}")
        print(f"Marks: {self.__marks}")

    def set_name(self, name):
        if name == "":
            print("Name cannot be empty")
        else:
            self.__name = name

    def set_rollno(self, rollno):
        if rollno < 1 or rollno > 100:
            print("Roll No must be between 1 and 100")
        else:
            self.__rollno = rollno

    def set_marks(self, marks):
        if marks < 0:
            print("Marks cannot be negative")
        else:
            self.__marks = marks


s1 = Student("Sahil", 16, 98)

s1.set_marks(90)
s1.set_rollno(20)
s1.set_name("Sahil Showkat")

s1.get_student()