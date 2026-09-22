# 3 types of string declear
name="sahil"
namee='sahil'
introd="""
My name is sahil
I'm from pulwama
and I am engineer
"""
trythis='hello "sahil" '
print(trythis)

#string in for loop
for character in name:
    print(character)

#String slicing
names="Sahil,Showkat"
print("lenth of a string =",len(names))
print(names[0:5])#0 sa 4 tak dega
fruit="sahil"
print(fruit[-4:-2])
#string operations
a="sahil!!!!"
length=len(a)
#string is immutaible, while upercasing its makes new string
print(a.upper())
print(a.lower())
print(a.replace("sahil","sahila"))
print(a.rstrip("!"))
b="sahil showkat"
print(b.split(" "))
blogheading="introduction to python"
print(blogheading.capitalize())
c="welcome to my desktop"
print(c.center(30))
print(c.count("e"))
d="my name is sahil showkat from dragad"
print(d.find("is"))

