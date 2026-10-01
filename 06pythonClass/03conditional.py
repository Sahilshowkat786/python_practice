num=int(input("Enter number: "))
if num >0:
    print("Positive number ")
    if num>0 and num<100:
        print("Number bt(1-100)")
elif num<0:
    print("Negative number ")
else:
    print("zero")


#conditions that are not ex
if True:
    print("always ex")

if "":
    print("python consider empty string False")
if 0:
    print("not,execute")

if None:
    print("not ex")

