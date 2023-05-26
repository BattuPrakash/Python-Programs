#length of longest increasing subsequence
def longest_increasing_subsequence(nums):
    n=len(nums)
    arr=[1]*n
    for i in range(1,n):
        for j in range(i):
           if nums[i]>nums[j]:
               arr[i]=max(arr[i],arr[j]+1)
    return max(arr)nn
nums=list(map(int,input().split()))
print("original list:")
print(nums)
print("length of longest increasing subsequence")
print(longest_increasing_subsequence(nums))
