def intersect(nums1, nums2):
    nums1Sort = sorted(nums1)
    nums2Sort = sorted(nums2)

    i, j = 0, 0

    interList = []

    while i < len(nums1Sort) and j < len(nums2Sort):
        if nums1Sort[i] < nums2Sort[j]:
            i += 1
        elif nums2Sort[j] < nums1Sort[i]:
            j += 1
        else:
            interList.append(nums1Sort[i])
            i += 1
            j += 1
    return interList

nums1 = [1,4,3,3,1]
nums2 = [10,3,3,2]

print(intersect(nums1, nums2))