n=int(input("Enter first no="))
m=int(input("Enter 2nd no="))
o=input("Enter operation we want to perform (+,-,*,/,//,%) =" )
if o=="+":
    print("the addition of two = ",n+m)
elif o=="-":
    print("The subtraction of two = ",n-m)
elif o=="*":
    print("The multiplication of two = ",n*m)
elif o=="/":
    print("The division of two = ",n/m)
elif o=="//":
    print("The floor value division of two = ",n//m)
else:
    print("The remainder of two = ",n%m)


