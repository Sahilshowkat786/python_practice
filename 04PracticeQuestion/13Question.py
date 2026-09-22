'''Average marks
Students scoring above average
Students scoring below average'''
students = {
    "Sahil": 85,
    "Rahul": 72,
    "Aman": 91,
    "Zaid": 65,
    "Adil": 88,
    "Arsalan":100
}
sum=0
for key,val in students.items():
    sum+=val
avg=sum/len(students)
print(f"Average marks are {avg}")


print("students scoring above avg are :")

for key,val in students.items():
    if val>avg:
        print(key,val)

print("students scoring below avg are :")
for key,val in students.items():
    if val<avg:
        print(key,val)



