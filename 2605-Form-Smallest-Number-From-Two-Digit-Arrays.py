class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)

        commons = s1&s2

        if commons:
            return min(commons)
        
        min1 = min(s1)
        min2 = min(s2)

        m1 = str(min1)+str(min2)
        m2 = str(min2)+str(min1)

        return min(int(m1), int(m2))
        
"""

Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.

"""