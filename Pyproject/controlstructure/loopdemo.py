l1 = [1,2,3,4,5,6,6,6,6]
l2 = [6,7,8,12,1,12,2]
l3 = ['a','b','c','d','e','f']

for a,b,c in zip(l1,l2,l3):
    print(a)
    print(b)
    print(c)

print(list(range(0,20,3)))

for a in range(3):
    print(a,a,sep="*")
