def checker(n):
    if(n>0 and n%2==0):
        print("Positive Even no")
    elif(n>0 and n%2!=0):
        print("Positive Odd no ")
    elif(n<0 and n%2==0):
        print("Negative Even no ")
    elif(n<0 and n%2!=0):
        print("Negative Odd no ")
    else:
        print("Zero")

n=int(input("Enter a number = "))
checker(n)