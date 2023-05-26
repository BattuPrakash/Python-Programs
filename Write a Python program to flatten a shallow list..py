import itertools
list1=[[2,4,3],[1,5,6],[9],[7,9,0]]
merge_list=list(itertools.chain(*list1))
print(merge_list)
