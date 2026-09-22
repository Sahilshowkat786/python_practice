'''
Write a Python program that takes 10 numbers from the user and:
Stores them in a list
Prints the largest number
Prints the smallest number
Prints the sum of all numbers
Counts how many even and odd numbers are present
'''
numbers = list(map(int, input("Enter 10 numbers = ").split()))

if len(numbers) != 10:
    print("Please enter exactly 10 numbers")
    exit()

largest = smallest = numbers[0]
sum = 0
evenCount = 0

for i in range(len(numbers)):
    sum += numbers[i]

    if numbers[i] >= largest:
        largest = numbers[i]

    if numbers[i] <= smallest:
        smallest = numbers[i]

    if numbers[i] % 2 == 0:
        evenCount += 1

oddcount = len(numbers) - evenCount

print(largest, smallest, sum, evenCount, oddcount)