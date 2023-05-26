n=int(input())
a=0
b=1
i=0
if n<=0:
    print("Enter a positive number")
elif n==1:
    print(a)
else:
    print("The fibanocii series")
    while i<n:
        print(a,end=' ')
        c=a+b
        a=b
        b=c
        i=i+1
    


