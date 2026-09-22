import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hrr=int(time.strftime('%H'))
hr=int(input("Enter hr of current time:"))
if(hr>=12 and hr<=16):
    print("Good Afternoon!!")
elif(hr>=4 and hr<=11):
    print("Good Morning!!")
elif(hr>=17 and hr<=20 ):
    print("Good Evening!!")
else:
    print("Good night!!")
