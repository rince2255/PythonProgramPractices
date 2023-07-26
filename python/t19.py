a=int(input("Enter the number : "))
flag=0
for i in range(1,int(a/2),1):
    if (a/2 %i==0):
        flag=1
        break
if(flag==0):
    print("prime number")
else:
    print("not prime")