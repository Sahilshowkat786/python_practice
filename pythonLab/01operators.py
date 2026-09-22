n1=int(input("Enter no1="))
n2=int(input("Enter no=2"))
print("Arithmatic operator(+,-,*,/,//,%)")
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1%n2)

print("logical operators(and or not)")
print(n1 and n2 )
print(n1 or n2)
print(not n1)

print("Relational operator (>,<,>= etc)")
print(n1>n2)
print(n1<n2)
print(n1>=n2)
print(n1<=n2)
print(n1==n2)
print(n1!=n2)

print("Assignement operator (=,+=,-= etc)")
n1+=5
print(n1)
n2*=2
print(n2)
#walrus operator
if(n:=n1>10):
    print("yes ")
else:
    print("no")
    
print("Bitwise operator (|,&,~)")
print(n1 | n2)
print(n1 & n2)
