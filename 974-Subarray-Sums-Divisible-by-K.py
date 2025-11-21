class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum=0
        pre_cnt=defaultdict(int)
        pre_cnt[0]=1
        res=0
        for n in nums:
            pre_sum+=n
            r = pre_sum % k
            res+=pre_cnt[r]
            pre_cnt[r]+=1
        return res

"""
Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:

Input: nums = [5], k = 9
Output: 0
"""