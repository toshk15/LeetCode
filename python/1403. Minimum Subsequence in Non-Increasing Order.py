class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sub=[]
        sumNums=sum(nums)
        res=0
        for n in nums:
            res+=n
            sumNums-=n
            sub.append(n)
            if res>sumNums:
                break
        return sub
            
