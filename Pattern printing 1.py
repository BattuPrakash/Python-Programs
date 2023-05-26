rows=int(input())
k=int(input())
for i in range(0,rows+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print(" ")

