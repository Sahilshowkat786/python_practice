# x=9 #global variable
# def fun():
#     x=2 #local variable
#     print(x)
# print(x)
# fun()

x=9 #global variable
def fun():
    global x
    x=5 #local variable
    print(x)
print(x)
fun()
print(x)