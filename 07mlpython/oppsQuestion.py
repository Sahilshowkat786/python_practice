class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count +=1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def final_amount(price,rate):
        discount_price=(price-(rate*price)/100)
        return discount_price

    
s=Product("Laptop",100)

s1=Product("smartWatch",78000)

s2=Product("ipad",145000)

s2.get_info()
s2.get_count()
print(s.final_amount(s.price,10))


