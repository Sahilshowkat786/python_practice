#fibonacci series 0,1,1,2,3,5,8,13,21,...
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(8))
# for i in range(10):
#     print(fib(i),end=",")


def fibser(n):
    a=0
    b=1
    for i in range(n):
       
        print(a,end=",")
        c=a+b
        a=b
        b=c
fibser(10)

   