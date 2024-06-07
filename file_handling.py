#read
# file=open(r'C:\Users\DELL\OneDrive\Desktop\file.txt','r')
# # x=file.read()
# # print(x)
#
# print(file.readline())
# # print(file.readlines())
# file.close()
#write
# write=open(r'C:\Users\DELL\OneDrive\Desktop\write.txt','w')
# # write.write('python')
# write.write('hello futura')

#append
# write=open(r'C:\Users\DELL\OneDrive\Desktop\write.txt','a')
# write.write('new append')


#x (use only for creating a new file)

# x=open(r'C:\Users\DELL\OneDrive\Desktop\x.txt','x')

#r+  can read and write
file=open(r'C:\Users\DELL\OneDrive\Desktop\file.txt','r+')
contant=file.read()
file.write('/nRplus learning')
print(contant)
file.close()


