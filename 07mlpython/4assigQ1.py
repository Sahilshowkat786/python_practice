class Bankaccount:
    def __init__(self,accountNo,ownerName,balance):
        self.accountNo=accountNo
        self.ownerName=ownerName
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount

    def checkBal(self):
        print("balance =",self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn")
            print(f"Remaining balance is {self.balance}")
        else:
            print("Insufficient balance")

a = Bankaccount("sb-192305","sahil",120)
a.deposit(1000)
a.checkBal()
a.withdraw(200)
a.checkBal()
        
