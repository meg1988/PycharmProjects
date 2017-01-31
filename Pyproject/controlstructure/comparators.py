"""
== --> equality operator
!= --> not equal to
<
>
<=
>=

"""

#if 100 < 10 :
#    print("first")
#elif 100 < 20 :
#    print ("second")
#else :
#    print ("third")

#print("great")

"""
x=0
while x<10:
    print("the value of x is " + str(x))
    x+=1

  #  if x == 8:
   #     break
    print("this is going good")
    print("**"*20)
else:
    print ("else is executed")

print("broke out of loop")

"""

my_string = "My name is Megha"
for c in my_string:
    print(c)


d={"one": 1, "two" : 2 , "three": 3}
for k in d:
    print(k + " " + str(d[k]))

print(d.items())

for k,v in d.items():
    print(k)
    print(v)
