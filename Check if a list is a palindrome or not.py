original_list1=list(map(str,input().split()))
list2=original_list1[::-1]
if original_list1==list2:
    print("list is palindrome")
else:
    print("list is not palindrome")
