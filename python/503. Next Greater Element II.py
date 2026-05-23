class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=[-1]*n
        for i in range(n*2-1,-1,-1):
            idx=i%n
            while stack and stack[-1]<=nums[idx]:
                stack.pop()
            if stack:
                res[idx]=stack[-1]
            stack.append(nums[idx])
        return res
        
