class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s=sum(nums)
        res=0
        l=0
        for n in nums[:-1]:
            l+=n
            r=s-l
            if (l-r)%2==0:
                res+=1
        return res
            
