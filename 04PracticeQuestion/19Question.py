class Library:
    books = []
    no_of_books = 0

    def __init__(self, name):
        Library.books.append(name)
        Library.no_of_books += 1

    @classmethod
    def show(cls):
        print("The books are in Library are :")
        for nam in cls.books:
            print(nam)
        print(f"The no of books are: {cls.no_of_books}")


l = Library("Python")
l = Library("Java")
l = Library("Math")
l = Library("Physics")
l = Library("SST")
l = Library("English")
l = Library("OOP")
l = Library("hands on Ml")

l.show()


