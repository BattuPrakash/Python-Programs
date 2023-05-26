table_num=int(input())
n=0
for i in range(1,13,1):
    product=table_num*i
    n+=1
    print(table_num,"*",n,"=",product)
