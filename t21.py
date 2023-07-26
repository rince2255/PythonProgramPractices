a=[1,3,5,7]
b=[2,4,6,8]
a=a+b
for i in range(0,len(a),1):
    for j in range(0, len(a) - i - 1,1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)