import random
yourScr=0
ComScr=0
for i in range(10):
    items = ["snake", "water", "gun"]
    computer = random.choice(items)

    user=input("Enter snake,water or gun : ").lower()

    print("computer choice :",computer)
    if(user=="snake" and computer=="water"):
        print("You Won !")
        yourScr+=1
    elif(user=="gun" and computer=="snake"):
        print("You Won !")
        yourScr+=1
    elif(user=="water" and computer=="gun"):
        print("You Won !")
        yourScr+=1
    elif(user=="water" and computer=="snake"):
        print("computer win !")
        ComScr+=1
    elif(user=="snake" and computer=="gun"):
        print("computer win !")
        ComScr+=1
    elif(user=="gun" and computer=="water"):
        print("computer win !")
        ComScr+=1
    else:
        print("Draw")
else:
    print("You score is ",yourScr)
    print("Computer's score is ",ComScr)
    quit()



