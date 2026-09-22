students = {
    "Sahil": 85,
    "Rahul": 78,
    "Aman": 92,
    "Zoya": 88,
    "Arjun": 81
}


def add_student():
    name = input("Enter student name: ").strip().title()

    if name in students:
        print("❌ Student already exists!")
        return

    marks = int(input("Enter marks: "))

    if 0 <= marks <= 100:
        students[name] = marks
        print(f"✅ {name} added successfully!")
    else:
        print("❌ Marks must be between 0 and 100.")


def update_marks():
    name = input("Enter student name: ").strip().title()

    if name not in students:
        print("❌ Student not found!")
        return

    marks = int(input("Enter new marks: "))

    if 0 <= marks <= 100:
        students[name] = marks
        print(f"✅ Marks updated for {name}!")
    else:
        print("❌ Marks must be between 0 and 100.")


def search_student():
    name = input("Enter student name: ").strip().title()

    if name in students:
        print(f"✅ {name} is present.")
        print(f"Marks: {students[name]}")
    else:
        print("❌ Student not found.")


def display_all():
    if not students:
        print("No students available.")
        return

    print("\n----- All Students -----")

    for name, marks in students.items():
        print(f"{name:<10} : {marks}")


while True:

    print("""
=============================
       STUDENT SYSTEM
=============================
A - Add Student
B - Update Marks
C - Search Student
D - Display All Students
E - Exit
=============================
""")

    option = input("Enter your option: ").upper().strip()

    match option:

        case "A":
            add_student()

        case "B":
            update_marks()

        case "C":
            search_student()

        case "D":
            display_all()

        case "E":
            print("\n👋 Program ended. Goodbye!")
            break

        case _:
            print("❌ Invalid option! Please choose A, B, C, D or E.")