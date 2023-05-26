
list1=list(map(int,input().split()))
dup_list=set()
uniq_list=[]
for i in list1:
    uniq_list.append(i)
    dup_list.add(i)
print(dup_list)
    
