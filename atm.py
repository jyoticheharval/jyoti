x,y=input().split(" ")
x=int(x)
y=float(y)
if (x%5==0 and x<(y-0.50)):
    z=y-x-0.50
    print('%2f'%z)
else:
    print('%2f'%y)
