"""
from collections import OrderedDict
def remove_duplicates(lst):
    return list(OrderedDict.frommkeys(lst))

nums=list(map(str,input().split()))
result=remove_duplicates(nums)
print(result)
"""
from collections import OrderedDict
def remove_duplicates(nums):
    return list(OrderedDict.fromkeys(nums))

nums = [1,2,4,3,5,4,6,9,2,1]
print("Original lists:")
print(nums)
result = remove_duplicates(nums)
print("Remove duplicates from the said list while preserving the order:")
print(result)
