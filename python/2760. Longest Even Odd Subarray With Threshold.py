class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        res=0
        for l in range(n):
            if nums[l]%2!=0:
                continue
            if nums[l]>threshold:
                continue
            for r in range(l,n):
                flag=True
                
                for j in range(l+1,r+1):
                    if nums[j]%2==nums[j-1]%2:
                        flag=False
                    if nums[j]>threshold:
                        flag=False
                if flag:
                   res=max(r-l+1,res)
        return res
