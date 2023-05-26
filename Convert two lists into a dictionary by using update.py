keys=list(map(str,input().split()))
values=list(map(int,input().split()))
res_dict=dict()
for i in range(len(keys)):
    res_dict.update({keys[i]:values[i]})
print(res_dict)
