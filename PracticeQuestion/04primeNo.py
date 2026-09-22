n=int(input("Enter a number= "))
def IsAPrimeNO(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==1):
        print("Not a prime no ")
    else:
        print("prime no ")

          
IsAPrimeNO(n)