# n1,n2,n3=map(int,input("Enter three numbers = ").split())
# if(n1>=n2 and n1>=n3):
#     print(n1," is greatest!!")
# elif(n2>=n1 and n2>=n3):
#     print(n2," is greatest!!")
# else:
#     print(n3," is greatest!!")

#leap year
n=int(input("enter year="))
if(n%400==0 or(n%4==0 and n%100 !=0)):
    print("yes ,it is leap year!!")
else:
    print("NO,it is not leap year ")