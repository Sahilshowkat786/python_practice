try:
    n=int(input("Enter a number: "))
    print(f"you age is {n}")
    l=[1,2,3]
    print(l[n])
    x=10/0
except ValueError:
    print("Please enter a valid number ")

except IndexError:
    print("Enter a valid index")
except:
# or 
# except ZeroDivisionError:
    print("something went wrong ")


#     try:
#     print("A")
#     x = 10 / 0
#     print("B")
# except:
#     print("C")

try:

    y=190/n
except ZeroDivisionError:
    print("zero division not possible ")
except Exception:
    print("some other exception ")

# else with exceptional handling
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success")
# finally
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("This always runs")