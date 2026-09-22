mylist=[1,2,3,4,"sahil",True,20.22]
print(mylist)
mylist.append(10)
print(mylist)
mylist.remove("sahil")
print(mylist)
mylist.reverse()
print(mylist)
print(mylist.count(2))
mylist.sort()
print(mylist)
mylist.pop(3)
print(mylist)
l2=[4,5,6,7]
#con two list
mylist.extend(l2)
print(mylist)
mylist.insert(0,"sahil")
print(mylist)
k=mylist+l2
print(k)
# mylist.sort(reverse=True)
# print(list)
print(len(k))
# mylist.clear()
del mylist[0]
print(mylist)

fromUser=list(map(int,input("Enter list = ").split()))
print(fromUser)