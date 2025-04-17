
f=open("test1.txt","r")
print(f.read())
f.close()
with open("test1.txt","r") as file:
    print(file.readlines())