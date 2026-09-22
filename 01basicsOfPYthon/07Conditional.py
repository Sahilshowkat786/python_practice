number=int(input("Enter number:"))
# if(number>18):
#     print("You are eligible")
# else:
#     print("You are not eligible")

#conditional elif
if(number<0):
    print("You entered negative number!!")
elif(number==0):
    print("You entered 0 ")
elif(number>0):
    print("You entered positive number!!")
    if(number>=0 and number<=10):
        print("you entered no between 1 to 10")
    elif(number>10 and number<=20):
        print("You entered no between 11 to 20 ")
    else:
        print("You entered no >20")
else:
    print("Enter a valid no ")