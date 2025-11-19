class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-2):           
            if (nums[i] + nums[i+2]) == nums[i+1]/2:
                c+=1
        return c
    

"""
Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

"""