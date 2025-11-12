from collections import Counter

def intersect(nums1, nums2):
    res = []
    c = Counter(nums1)
    for i in nums2:
        if i in c:
           if c[i] > 0:
            res.append(i)
            c[i]-=1
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1, nums2))