import os

files=[f for f in os.listdir() if f.lower().endswith(".png")]
print(files)
for i , file in enumerate(files,start=1):
    os.rename(file,f"Image_{i}.png")
print("Done !")