# ============================================================
#                  PYTHON FILE I/O
#              Beginner → Advanced
# ============================================================


# ------------------------------------------------------------
# 1. OPENING A FILE
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file)

file.close()


# ------------------------------------------------------------
# 2. READING ENTIRE FILE
# ------------------------------------------------------------

file = open("example.txt", "r")

data = file.read()

print(data)

file.close()


# ------------------------------------------------------------
# 3. READING A SPECIFIC NUMBER OF CHARACTERS
# ------------------------------------------------------------

file = open("example.txt", "r")

data = file.read(10)

print(data)

file.close()


# ------------------------------------------------------------
# 4. READ ONE LINE
# ------------------------------------------------------------

file = open("example.txt", "r")

line = file.readline()

print(line)

file.close()


# ------------------------------------------------------------
# 5. READ MULTIPLE LINES
# ------------------------------------------------------------

file = open("example.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ------------------------------------------------------------
# 6. LOOP THROUGH FILE
# ------------------------------------------------------------

file = open("example.txt", "r")

for line in file:
    print(line.strip())

file.close()


# ------------------------------------------------------------
# 7. WRITE TO A FILE
# ------------------------------------------------------------

file = open("write.txt", "w")

file.write("Hello Python!")

file.close()


# ------------------------------------------------------------
# 8. WRITE MULTIPLE LINES
# ------------------------------------------------------------

file = open("write.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

file.close()


# ------------------------------------------------------------
# 9. writelines()
# ------------------------------------------------------------

lines = [
    "Apple\n",
    "Banana\n",
    "Mango\n"
]

file = open("fruits.txt", "w")

file.writelines(lines)

file.close()


# ------------------------------------------------------------
# 10. APPEND MODE
# ------------------------------------------------------------

file = open("write.txt", "a")

file.write("\nThis is appended text.")

file.close()


# ------------------------------------------------------------
# 11. CREATE A NEW FILE USING x
# ------------------------------------------------------------

# This gives an error if the file already exists.

# file = open("newfile.txt", "x")
# file.write("New file created")
# file.close()


# ------------------------------------------------------------
# 12. WITH STATEMENT
# ------------------------------------------------------------

with open("example.txt", "r") as file:
    data = file.read()
    print(data)

# File automatically closes here.


# ------------------------------------------------------------
# 13. CHECK WHETHER FILE IS CLOSED
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file.closed)

file.close()

print(file.closed)


# ------------------------------------------------------------
# 14. FILE MODE
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file.mode)

file.close()


# ------------------------------------------------------------
# 15. FILE NAME
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file.name)

file.close()


# ------------------------------------------------------------
# 16. FILE POSITION / tell()
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file.tell())

data = file.read(5)

print(data)

print(file.tell())

file.close()


# ------------------------------------------------------------
# 17. seek()
# ------------------------------------------------------------

file = open("example.txt", "r")

print(file.read(5))

file.seek(0)

print(file.read(5))

file.close()


# ------------------------------------------------------------
# 18. SEEK TO SPECIFIC POSITION
# ------------------------------------------------------------

file = open("example.txt", "r")

file.seek(10)

print(file.read())

file.close()


# ------------------------------------------------------------
# 19. READ + WRITE (r+)
# ------------------------------------------------------------

file = open("example.txt", "r+")

data = file.read()

print(data)

file.write("\nNew content")

file.close()


# ------------------------------------------------------------
# 20. WRITE + READ (w+)
# ------------------------------------------------------------

file = open("test.txt", "w+")

file.write("Hello")

file.seek(0)

print(file.read())

file.close()


# ------------------------------------------------------------
# 21. APPEND + READ (a+)
# ------------------------------------------------------------

file = open("test.txt", "a+")

file.write("\nPython")

file.seek(0)

print(file.read())

file.close()


# ------------------------------------------------------------
# 22. BINARY FILES
# ------------------------------------------------------------

# rb = read binary
# wb = write binary

file = open("example.jpg", "rb")

data = file.read()

print(data)

file.close()


# ------------------------------------------------------------
# 23. COPY A BINARY FILE
# ------------------------------------------------------------

with open("example.jpg", "rb") as source:
    data = source.read()

with open("copy.jpg", "wb") as destination:
    destination.write(data)


# ------------------------------------------------------------
# 24. EXCEPTION HANDLING WITH FILES
# ------------------------------------------------------------

try:
    with open("does_not_exist.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist!")


# ------------------------------------------------------------
# 25. DIFFERENT FILE ERRORS
# ------------------------------------------------------------

try:
    file = open("example.txt", "r")

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permission denied!")

finally:
    print("File operation finished.")


# ------------------------------------------------------------
# 26. CHECK IF FILE EXISTS
# ------------------------------------------------------------

import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")


# ------------------------------------------------------------
# 27. DELETE A FILE
# ------------------------------------------------------------

# import os

# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File deleted")
# else:
#     print("File doesn't exist")


# ------------------------------------------------------------
# 28. GET FILE SIZE
# ------------------------------------------------------------

import os

if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")

    print("File size:", size, "bytes")


# ------------------------------------------------------------
# 29. RENAME A FILE
# ------------------------------------------------------------

# import os

# os.rename("old.txt", "new.txt")


# ------------------------------------------------------------
# 30. CURRENT WORKING DIRECTORY
# ------------------------------------------------------------

import os

print(os.getcwd())


# ------------------------------------------------------------
# 31. LIST FILES IN CURRENT DIRECTORY
# ------------------------------------------------------------

print(os.listdir())


# ------------------------------------------------------------
# 32. CREATE DIRECTORY
# ------------------------------------------------------------

# import os

# os.mkdir("my_folder")


# ------------------------------------------------------------
# 33. CREATE DIRECTORY SAFELY
# ------------------------------------------------------------

# import os

# os.makedirs("folder1/folder2", exist_ok=True)


# ------------------------------------------------------------
# 34. DELETE EMPTY DIRECTORY
# ------------------------------------------------------------

# import os

# os.rmdir("my_folder")


# ------------------------------------------------------------
# 35. pathlib MODULE
# ------------------------------------------------------------

from pathlib import Path

path = Path("example.txt")

print(path.exists())


# ------------------------------------------------------------
# 36. READ USING pathlib
# ------------------------------------------------------------

path = Path("example.txt")

if path.exists():
    data = path.read_text()

    print(data)


# ------------------------------------------------------------
# 37. WRITE USING pathlib
# ------------------------------------------------------------

path = Path("hello.txt")

path.write_text("Hello from pathlib!")


# ------------------------------------------------------------
# 38. APPEND USING pathlib
# ------------------------------------------------------------

with path.open("a") as file:
    file.write("\nNew line")


# ------------------------------------------------------------
# 39. FILE SUFFIX / EXTENSION
# ------------------------------------------------------------

path = Path("example.txt")

print(path.suffix)


# ------------------------------------------------------------
# 40. FILE NAME
# ------------------------------------------------------------

print(path.name)


# ------------------------------------------------------------
# 41. FILE PARENT DIRECTORY
# ------------------------------------------------------------

print(path.parent)


# ------------------------------------------------------------
# 42. LIST .TXT FILES
# ------------------------------------------------------------

for file in Path(".").glob("*.txt"):
    print(file)


# ------------------------------------------------------------
# 43. CSV FILE
# ------------------------------------------------------------

import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerow(["Sahil", 20, 90])
    writer.writerow(["Rahul", 21, 85])


# ------------------------------------------------------------
# 44. READ CSV
# ------------------------------------------------------------

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ------------------------------------------------------------
# 45. JSON FILE
# ------------------------------------------------------------

import json

student = {
    "name": "Sahil",
    "age": 20,
    "skills": [
        "Python",
        "C++",
        "Machine Learning"
    ]
}

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)


# ------------------------------------------------------------
# 46. READ JSON
# ------------------------------------------------------------

with open("student.json", "r") as file:

    data = json.load(file)

print(data)

print(data["name"])


# ------------------------------------------------------------
# 47. UPDATE JSON
# ------------------------------------------------------------

with open("student.json", "r") as file:
    data = json.load(file)

data["age"] = 21

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)


# ------------------------------------------------------------
# 48. ENCODING
# ------------------------------------------------------------

with open(
    "unicode.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("Hello Sahil 😊")


# ------------------------------------------------------------
# 49. READ WITH ENCODING
# ------------------------------------------------------------

with open(
    "unicode.txt",
    "r",
    encoding="utf-8"
) as file:

    print(file.read())


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

"""
Main File Modes:

r   -> read
w   -> write / overwrite
a   -> append
x   -> create
r+  -> read + write
w+  -> write + read
a+  -> append + read

Binary:

rb  -> read binary
wb  -> write binary

Important methods:

read()
read(n)
readline()
readlines()
write()
writelines()
seek()
tell()
close()

Useful modules:

os
pathlib
csv
json

Best general pattern:

with open("file.txt", "r", encoding="utf-8") as file:
    data = file.read()

"""

print("\nFILE I/O COMPLETE")