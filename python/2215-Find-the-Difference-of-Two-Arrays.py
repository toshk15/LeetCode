def findDifference(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    res1=[]
    res2=[]
    for num in nums1_set:
        if num not in nums2_set:
            res1.append(num)
    
    for num in nums2_set:
        if num not in nums1_set:
            res2.append(num)

    return [res1, res2]

nums1=[1,2,3,3]
nums2=[2,4,6,4]

print(findDifference(nums1, nums2))