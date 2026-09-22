cube=lambda x:x*x*x
print(cube(3))

#fun as an argunment
def fun(fx,val):
    return 4+fx(val)
print(fun(cube,3))
