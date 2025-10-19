a=int(input())
b=int(input())
if  (a+b)%4==0:
    print(a+b)
elif (a+b)%4==1:
    print(a-b)
elif (a+b)%4==2:
    print(a*b)
else:
    print(a/b)
