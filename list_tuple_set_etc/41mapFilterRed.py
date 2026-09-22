# map
lis=[1,2,3,4,14,6]
sq=lambda x:x*x
newlist=list(map(sq,lis))
print(newlist)

#filter
newl=list(filter(lambda x:x%2==0,lis))
print(newl)

#reduce
from functools import reduce
sum=reduce(lambda x,y:x+y,lis)
print(sum)