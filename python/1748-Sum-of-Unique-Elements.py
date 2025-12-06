class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c=Counter(nums)
        s=0
        for i,j in c.items():
            if j==1:
                s+=i
            else:
                continue
        return s

"""
Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

"""