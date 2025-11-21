class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumT=0
        indexmap=defaultdict(int)
        indexmap[0]=-1

        for i,j in enumerate(nums):
            sumT+=j
            remaider = sumT%k
            if remaider not in indexmap:
                indexmap[remaider]=i
            elif i-indexmap[remaider]>1:
                return True
        return False
    

"""
Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

"""