a=tuple(("apple","mango","kiwi"))
b=tuple(("car","bike","jeep","bus"))
#printing
#print(a)

#slicing
#print(a[:])
#print(a[-2:-1])

#changing tuple to list
c=list(a)
#print(c)
#print(type(c))

c[1]=("banana")
#print(c)
a=tuple(c)
print(a)
print(type(a))



