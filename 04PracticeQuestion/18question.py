import random

key = random.randint(1, 100)
attempt = 0

while True:
    number = int(input("Enter number between (1-100): "))

    if number < 1 or number > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempt += 1

    if number > key:
        if number - key < 6:
            print("Too close!")
        else:
            print("Too high!")

    elif number < key:
        if key - number < 6:
            print("Too close!")
        else:
            print("Too low!")

    else:
        print("You win!")
        break

print(f"You used {attempt} attempts to reach the goal.")