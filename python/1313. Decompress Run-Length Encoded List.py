class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(nums):
            while nums[i]>0:
                res.append(nums[i+1])
                nums[i]-=1
            i+=2
        return res
