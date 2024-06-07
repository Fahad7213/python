find=input("enter the finding value")
a=["red","blue","pink","black"]
for i in a:
    if  i==find:
        print(i)
    else:
        print("not found")

if "red" in a:
    print("present")
else:
    print("not found")