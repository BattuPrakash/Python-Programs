list1=list(map(int,input().split()))
small_num=9999999999999999999
for i in list1:
    if i<small_num:
        small_num=i
print(small_num)
    
