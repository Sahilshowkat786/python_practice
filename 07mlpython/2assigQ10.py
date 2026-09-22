'''Ask the user for a string and print
• All unique characters
• The count of unique character'''
user_input=input("Enter string = ")
li=[]
count=0

for ch in user_input:
     li.append(ch)


unique=set(li)

print("The unique characters are : ",unique)
print("No of unique characters are : ",len(unique))
