# lmb=lambda a,b,c: print(a+b+c)
#
# lmb(2,2,2,)

# lmb=lambda a,b,c:a+b+c
#
# print(lmb(2,2,2))

#lambda function in function
# def fun(b):
#     return lambda a:a*b
# y=fun(10)
# print(y(2)

#recursive fun
def fun(a):
    if a<=1:
        return 1
    else:
        return a*(fun(a-1))
print(fun(3))