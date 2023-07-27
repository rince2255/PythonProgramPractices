a=[1,2,7,3,9,4,6]
larg=a[0]
for i in range(0,len(a)):
    if a[i] > larg:
        larg = a[i]
print(larg)

a=[1,2,7,3,9,4,6]
larg=a[0]
for i in range(0,len(a)):
    if a[i] < larg:
        larg = a[i]
print(larg)