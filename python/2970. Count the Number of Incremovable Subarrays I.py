class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                arr=nums[:i]+nums[j+1:]
                flag=True
                for x in range(1,len(arr)):
                    if arr[x]<=arr[x-1]:
                        flag =False
                        break
                if flag:
                    res+=1
        return res
                
                
