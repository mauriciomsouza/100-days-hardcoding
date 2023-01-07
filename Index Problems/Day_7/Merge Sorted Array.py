def MergeSortedArray(nums1,m, nums2, n):
    if len(nums1) == m+len(nums2):
        return sorted(nums2 + nums1[0:m])
    else:
        return None


m = 3
nums1 = [1,2,3,0,0,0]
n = 3 
nums2 = [2,5,6]


print(MergeSortedArray(nums1, m, nums2, n))
