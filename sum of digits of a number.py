
def ComputeSum(num):
    sum=0
    for digit in str(num):
        sum+=int(digit)
    return sum

num=int(input("enter a number "))

print('sum of digits in a number =',ComputeSum(num))


