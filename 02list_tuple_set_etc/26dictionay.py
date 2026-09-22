dic={
    "Sahil":"Sahil is my name",
    "spoon":"object"
}
print(dic["Sahil"])
print(dic.keys())
print(dic.values())
info={
    1:"jibran",
    2:"Moomin",
    3:"Faizan",
    4:"zoya",
    5:"tehreem",
    6:"Sahil",
    7:"Arsalan",
    8:"ishfaq"
}

for key in info.keys():
    print(info[key])
for key,val in info.items():
    print(f"The value corresponding to the key {key} is {val}")
print(info[6])

empty={}
print(empty)
print(type(empty))