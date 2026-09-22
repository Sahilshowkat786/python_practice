# readline
f=open("file.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)

# write lines
f=open("file.txt","w")
list=["line 1\n","line2\n","line3\n"]
f.writelines(list)
f.close()

# seek fun
with open("file.txt","r") as f:
    f.seek(3)#position 3 sa start karaga
    data=f.read(10)
    print(data)
#tell fun
#it returns current position in file
    print(f.tell())   # it gives 10

#truncate fun
f=open("file.txt","r")
f.truncate(5) #it gives only first 5 bytes in file.txt
f.close()