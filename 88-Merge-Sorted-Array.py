"""
def merge(L1, m, L2, n):
    max_size = m + n -1

    while n >= 0 and m>=0:

        if L1[m-1] < L2[n-1]:
            L1[max_size] = L1[m-1]
            m -= 1            
        else:
            L1[max_size] = L2[n-1]
            n -= 1
        max_size -= 1

    return L1
"""
"""
def merge(L1, m, L2, n):
    res = [None] * (m + n)
    while m > 0 and n > 0:
        if L1[m-1] >= L2[n-1]:
            res[m+n-1] = L1[m-1]
            m -= 1
        else:
            res[m+n-1] = L2[n-1]
            n -= 1
    #print(res)
    if n > 0:
        res[:m+n] = L2[:n] 
    if m > 0:
        res[:m+n] = L1[:m]  
    return res   

"""

def merge(nums1, m, nums2, n):
        
    while m>0 and n>0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m-=1
        else:
            nums1[m+n-1] = nums2[n-1]
            n-=1
            
    while m>0:
        nums1[m+n-1] = nums1[m-1]
        m-=1
            
    while n>0:
        nums1[m+n-1] = nums2[n-1]
        n-=1            
    return nums1


    


L1 = [1,2,4,7,8]
L2 = [3,5,6]

print(merge(L1, 5, L2, 3))


"""
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""