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


"""
Example 1:

Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

Example 2:

Input: nums = [1,1,1,1]
Output: false
Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

"""