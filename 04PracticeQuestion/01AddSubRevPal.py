n=int(input("Enter number:"))
a=n
addition=0
multiple=1
rev=0
count=0
while(n>0):
    num=n%10
    rev=rev*10+num
    addition+=num
    multiple*=num
    n=n//10
    count=count+1
print("The sum of digits =",addition)
print("The product of digits =",multiple)
print("Reverse of a no = ",rev)
if(a==rev):
    print("pallandrome")
print("count=",count)

