def union_intersection(nums1,nums2):
    union=list(set(nums1) | set(nums2))
    intersection=list(set(nums1)& set(nums2))
    return union,intersection

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(union_intersection(nums1,nums2))
