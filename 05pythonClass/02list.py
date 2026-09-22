list=["sahil",19,True,(2,2),340000.33]
print(list)
#list are mutable in nature ,allow duplicate values
#ordered
print(len(list))
#constructor list
thislist=(("sahil",12,"age"))
print(thislist)
print("i in sahil =",thislist[0][3])
# listi=map(list,input("enter list = ").split())
# print(listi)
list[3]="complex no"
print(list)
list[5:7]=["apple","ball"]
print(list)
#add in a list
list.append("last element")
print(list)
# thislist.extend(list)
# print(thislist)

#remove elements from list
list.remove("sahil")

list.pop(3) #location 3 is removed

list.pop() #bydefault end valued is removed 

list.clear()#remove all list
list.append("deleteThisonce")
#del using indexing
del list[0]
print(list)

#list
lst = list(map(int, input("Enter numbers: ").split()))
print(lst)

