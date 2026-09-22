try:
    n=list(map(int,input("Enter list : ").split()))
    print(n)
    print(n[2])
except IndexError:
    print("Enter a valid index")
except :
    print("something happened here !")
else:
    print("i am done with no error ")
finally:
    print("i am always exceuted ")