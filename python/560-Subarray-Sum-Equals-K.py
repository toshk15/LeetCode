class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum=0
        d = defaultdict(int)
        res=0     
        d[0]=1

        for n in nums:
            prev_sum += n
            diff = prev_sum - k
            res+=d[diff] 
            d[prev_sum]+=1             
            
        return res
        

"""
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""