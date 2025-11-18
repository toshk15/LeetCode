class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]

        def backtrack(i):
            if i==len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)
        backtrack(0)
        return res
    
"""
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
"""