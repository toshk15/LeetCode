def addedInteger(nums1,nums2):
    if not nums1 or not nums2:
        return 0
    nums1.sort()
    nums2.sort()
    res = nums2[0]-nums1[0]
    return res