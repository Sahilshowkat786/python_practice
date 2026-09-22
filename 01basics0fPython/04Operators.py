#1.Arithmatic oprators 
n1=int(input("Enter no1="))
n2=int(input("Enter no2="))
print("addition of two = ",n1+n2)
print("subtraction of two = ",n1-n2)
print("multiplication of two = ",n1*2)
print("division of two = ",n1/n2)
print("exact division floor of two = ",n1//n2)
print("remender of two = ",n1%n2)

#2.relational operator
print(2>1)
print(45<1)
print(56==56)

#3.logical operator
print(5>=2 or 8<=10)
# and ,not

#4.Bitwise operator
print(12 & 11)
# |,^,~,<<,>>

#5.assignment operator 
n1 += 5
print(n1)
# = , *=, %=

#6.membership operatior(in, not in)
name = "Sahil"
print("S" in name)
print("Z" in name)
print("a" not in name)

#7.identity operator
a=[1,3]
b=a
print(a is b)
print(a is not b)
