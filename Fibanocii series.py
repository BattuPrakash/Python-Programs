num=int(input())
a,b=0,1
i=0

if num<0:
    print("Enter a positive integer")
elif num==1:
    print("The Fibanocii series")
    print(a)
else:
    print("The Fibanocii series")
    while i<num:
        print(a,end=' ')
        c=a+b
        a=b
        b=c
        i=i+1
