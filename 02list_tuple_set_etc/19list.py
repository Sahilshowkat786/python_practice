# list=[1,3,4]
# print(list[:])
# print(list[2])
# print(list[-3]) #negative nidex
# if 3 in list:
#     print("yes")
# else:
#     print("no")

#jump index
marks=[1,2,3,4,5,6,7,8,9]
print(marks[1:8:3])
#list comprehension
# lst=[i for i in range(5)]
# print(lst)
lst=[i for i in range(5) if i%2==0]
print(lst)