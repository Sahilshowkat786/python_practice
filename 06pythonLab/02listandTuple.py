lis=[1,2,1,3,4,5,6,"sahil"]
print(type(lis))
print(lis)
lis.append("last")
print(lis)
lis.pop(3)
print(lis)
lis.index("sahil")
print(lis)
l2=[]
# lis.copy(l2)
# print(l2)
lis.remove("sahil")
print(lis)
print(lis.count(1))
del lis[-1]
print(lis)
print(len(lis))
lis.insert(0,"firstElement")
print(lis)
lis[-1]="lastele"
print(lis)
l2=["y","e","s"]
lis.extend(l2)
print(lis)
l=[2,4,6,7,1,10]
l.sort()
print(4)
print(l.index(1))
l=[1,4,5]
l=lis.copy()
print(l)
del l,lis