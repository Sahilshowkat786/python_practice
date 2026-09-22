#one liner if else shorthand
a=10
b=45
c=a if a>b else b
print(c)

# == vs is 


a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)
print(a==b)

a=(1,2,3)
b=(1,2,3)
print(a is b)
print(a==b)

a=5
b=a
print(a==b)
print( a is b)