#reverse the list at specifed location
list1=list(map(int,input().split()))
print("The original list is :",list1)
start_pos=int(input())
end_pos=int(input())
while start_pos < end_pos:
    list1[start_pos],list1[end_pos]=list1[end_pos],list1[start_pos]
    start_pos+=1
    end_pos-=1
print(list1)
