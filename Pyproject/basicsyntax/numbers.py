int_num = 5
float_num = 10.81

int_num=float_num

print(int_num)
print(float_num)

a=10
b=30

add=a+b
print(add)

sub=a-b
print(sub)

mul=a*b
print(mul)

div=a/b
print(div)

# this is a one line comment

""" this is multiline
comment

"""

print(10**20)

print(100%3)

c=None
a= bool(0)
b= bool(100)

print(a)
print(b)
print(bool(c))


"""
Strings

"""

a= "this is a single \
string"

print(a)

first="nyc"
print(first[0])

"""
len()
upper()
lower()
str()
"""

stri = "THIS IS A mixed case"
print(stri.lower())
print(stri.upper())
print(len(stri))

a=10
print(a)
print(str(a))
print(stri + str(a))

a="My name is Megha Rastogi"
print(a.replace("a","b"))
print(a[1:20:1])
print(a[1:20:3])

print(a[::-1])


city="sfo"
event="coldplay concert"

print("Welcome to %s to attend the %s" %(city,event))