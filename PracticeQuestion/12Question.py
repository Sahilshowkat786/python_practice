'''
Write a program to:
Print all subjects
Print all marks
Calculate total marks
Calculate average marks
Find the highest mark
Find the lowest mark
'''
marks={
    "dsa":90,
    "c++":84,
    "python":95,
    "dbms":15,
    "c":66
}
print("printing all subjects :")
for key,val in marks.items():
    print(key)


total=0
highest=0
lowest=100
print("printing all marks :")
for key,val in marks.items():

    total+=marks[key]

    avg=total/len(marks)

    print(marks[key])

    if marks[key]>=highest:
        highest=marks[key]

    if marks[key]<=lowest:
        lowest=marks[key]

print(f"Total marks are {total} out of 500")
print(f"Average marks : {avg}")
print(f"The lowest marks are {lowest} and highest are {highest}")
