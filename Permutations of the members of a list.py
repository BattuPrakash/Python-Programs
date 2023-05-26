import itertools
list1=list(map(int,input().split()))
permu=list(itertools.permutations(list1))
print(permu)
