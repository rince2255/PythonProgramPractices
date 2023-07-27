a = ['abc', 'xyz', 'aba', '1221']
count=0
b=[]
for i in a:
    if (len(i) >= 2) and (i[0] == i[-1]):
        b.append(i)
        count+=1
print(count)
print(b)