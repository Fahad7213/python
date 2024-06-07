# a=[1,2,3,4,5,6,7,8,9,10]
# odd=[]
# even=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# a=[1,2,3,4,5,6,7,8,9,10]
# list1=[i for i in a if i%2==0]
# print(list1)
# list2=[i for i in a if i%2!=0]
# print(list2)

#palindrome
# a=[101]
# pl=[i for i in a if i[:]==i[-1: ]]
# print(pl)

#palindrome
list=['malayalam','mom','son','deer','pep']
list1=[i for i in list if i==i[::-1]]
print(list1) 



