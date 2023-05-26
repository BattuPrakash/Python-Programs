list1=list(map(str,input().split()))
list2=list(map(str,input().split()))
common_list=[]
for i in list1:
    if i in list2:
        common_list.append(i)
print(common_list)
