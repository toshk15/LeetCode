class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        accu_sum=0
        max_accu=0
        l=0
        seen=set()
        for r in range(len(nums)):
            while nums[r] in seen:
                accu_sum-=nums[l]
                seen.remove(nums[l])
                l+=1
            seen.add(nums[r])
            accu_sum+=nums[r]
            max_accu=max(max_accu, accu_sum)
        return max_accu
                
            
