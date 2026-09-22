info={
    ("sahil","math"),
    ("arsalan","science"),
    ("sahil","science"),
    ("ishfaq","math"),
    ("arsalan","math"),
    ("sahil","english"),
    ("ishfaq","english")
}
# 1.list all unique course
courses_set=set()
# for tup in info:
#     courses_set.add(tup[1])
# print(courses_set)

# 2. list students enrolled in english
# for val in info:
#     if(val[1]=="english"):
#         print(val[0])

#3.  create dict (student,set of courses)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
    
print(dict)