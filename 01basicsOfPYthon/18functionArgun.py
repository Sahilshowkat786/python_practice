def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The avg is = ",sum/len(numbers))
avg(1,2,3,6)
avg(3,4)