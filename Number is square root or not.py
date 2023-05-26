import math
num=int(input())
root=math.sqrt(num)
if int(root+0.5)**2 == num:
    print(num," is the perfect square")
else:
    print(num,"is not perfect square")

