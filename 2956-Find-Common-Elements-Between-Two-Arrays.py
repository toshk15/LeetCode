class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                d1[nums1[i]]+=1          
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                d2[nums2[j]]+=1  
        s1 = sum(d1.values())  
        s2 = sum(d2.values()) 
        res.append(s1)  
        res.append(s2)        
        return res
    
"""
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ansers = [0,0]
        un1 = set(nums1)
        un2 = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in un2:
                ansers[0] += 1
        for i in range(len(nums2)):
            if nums2[i] in un1:
                ansers[1] +=1
        return ansers
"""
    
"""
Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]

Explanation:

Example 2:

Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

Output: [3,4]

Explanation:

The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

Example 3:

Input: nums1 = [3,4,2,3], nums2 = [1,5]

Output: [0,0]

Explanation:

No numbers are common between nums1 and nums2, so answer is [0,0].

"""