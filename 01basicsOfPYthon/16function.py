def add(a,b):
    sum=a+b
    print("The sum of two numbers are ",sum)

n1,n2=map(int,(input("Enter two numbers=").split()))

add(n1,n2)

# when user have to work after sometime on a function, he used pass
# without pass intrepeter throughs error
def sub(a,b):
    pass

def name():
    return"sahil showkat"
print(name())