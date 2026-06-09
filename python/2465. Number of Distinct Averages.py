class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avg=0
        l=0
        seen=set()
        r=len(nums)-1
        while l<=r:
            avg = (nums[l]+nums[r])/2
            if avg not in seen:
                seen.add(avg)
            l+=1
            r-=1
        return len(seen)
                
                
