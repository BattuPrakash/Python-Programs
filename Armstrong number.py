def digits_count(n):
    i=0
    while n>0:
        n=n//10
        i=i+1
    return i
def sum(n):
    i=digits_count(n)
    s=0
    while n>0:
        digit=n%10
        n=n//10
        s=s+pow(digit,i)
    return s

num=int(input("Enter the number"))
s=sum(num)
if s==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")

