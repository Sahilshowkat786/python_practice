'''
Take a sentence from the user and:

Find all unique words using a set
Print the number of unique words
Print the unique words in alphabetical order
'''

sen = input("Enter sentence: ")

senList = sen.split()

temp = set(senList)

count = len(temp)

print("Unique words:", temp)
print("Total unique words:", count)
print("Alphabetical order:", sorted(temp))

