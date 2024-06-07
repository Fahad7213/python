import re

txt="the rain kannur"
x= re.search("n",txt)
# print(x)
print(x.span())
# print(x.string)
# print(x.group())
