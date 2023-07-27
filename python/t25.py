a=[3,0,2,1,0,8,0,0]
b=[]
c=[]
for i in range(0,len(a)):
    if a[i]!=0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b+c)