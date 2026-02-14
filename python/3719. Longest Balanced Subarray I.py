class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            even={}
            odd={}
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    even[nums[j]]=even.get(0,nums[j])+1
                else:
                    odd[nums[j]]=odd.get(0,nums[j])+1
                if len(even)==len(odd):
                    res=max(res,j-i+1)
            if len(nums)==res:
                break
        return res
