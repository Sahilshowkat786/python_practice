user_entered=input("Enter the word : ").strip()
data=True
count=0
with open("file.txt","r") as f:
    while data:
        count+=1
        data=f.readline()
        if(f"{user_entered}" in data):
                print(f"Yes,{user_entered} found at line no {count} ")
                break
    else:
        print("not found in file.txt")