''''
num=int(input("Enter the number"))
original=num
rev=0
i=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if rev==original:
    print("it is a palindrime")
else:
    print("it is not a palindrome")
    
'''''

num=int(input("Enter the number "))
original=num
reverse=int(str(num)[::-1])
if original==reverse:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
