class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n*2
        for i in range(n):
            res[i]=nums[i]
        j=0
        for i in range(2*n-1,n-1,-1):
            print(i)
            res[i]=nums[j]
            j+=1
        return res
