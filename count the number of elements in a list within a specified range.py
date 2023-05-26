list1=list(map(int,input().split()))
start=int(input())
end=int(input())
count=0
for i in list1:
    if start<=i<=end:
        count+=1
print(count)
        
