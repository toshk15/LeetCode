class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)-1):
           n=nums[i]+nums[i+1]
           if n in seen:
              return True
           seen.add(n)
        return False
           
