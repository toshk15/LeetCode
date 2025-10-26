from collections import Counter

def isPossibleToSplit(nums):
    c = Counter(nums)

    for i,j in c.items():
        if j>2:
            return False
    return True


   """
   nums1=[]
    nums2=[]
    f=0
    for i in nums:
        if f==0:
            nums1.append(i)
            f=1
            continue
        if f==1:
            nums2.append(i)
            f=0
            continue

    if len(nums1)==len(nums2) and nums1 != nums2:
        return True
    else:
        return False
   """
    

nums = [6,1,3,1,1,8,9,2]
print(isPossibleToSplit(nums))