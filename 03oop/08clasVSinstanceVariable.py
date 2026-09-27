class Employee:
    companyName="Apple"
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.3

    def show_detail(self):
        print(f"The employee name is {self.name} and raise amount {self.raise_amount} in {self.companyName}")

emp1=Employee("sahil")
emp2=Employee("Arsalan")
emp1.show_detail()
emp2.companyName="Tesla"
print(Employee.companyName)
emp2.show_detail()

# Employee.show_detail(emp1)
