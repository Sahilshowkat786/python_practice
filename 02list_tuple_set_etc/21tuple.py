# t=(1)
# print(type(t))
t=(1,)
print(type(t))
tup=(1,2,3,5,"ahil",True)
print(tup)
print(tup[3])
#tuples are immutable ,they cannot be changed ,first convert into list
temp=list(tup)
temp.append("lastElement")
temp.pop(3)
temp.remove("ahil")
temp.insert(3,"anis")
temp.append(10)
tup=tuple(temp)
print(tup)
#methods in tuple
L=len(tup)
print(L)
tup2=(8,9,10)
tup3=tup+tup2
print(tup3)
print(tup3.index(9))
print(tup3.count(10))

# i can delete whole tuple using tup del
del tup,tup2,tup3
