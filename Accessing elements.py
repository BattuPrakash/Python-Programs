import array as arr
a=arr.array('i',[1,2,3,4,5,6,7])
print("Access element is:",a[0])
print("The popped element is:",a.pop(0))
for i in a:
    print(i)
