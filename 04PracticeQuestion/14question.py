# try exceptional handling 
try:
    n=int(input("Enter a number: "))
    res=100/n
except ValueError:
    print("Invalid number ")
except ZeroDivisionError:
    print("division by 0 not possible ")
else:
    print(f"The result is {res}")
finally:
    print("program finished !!")
