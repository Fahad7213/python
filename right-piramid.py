num=int(input("enter a num"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(num,1,-1):
    print("* "*(i))