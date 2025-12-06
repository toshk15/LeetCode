from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        r=len(nums)
        
        res=[]
        c = len(max(nums, key=len))
    
        for i in range(r):
            for j in range(c):
                if j<len(nums[i]):
                    d[i+j].append(nums[i][j])
                else:
                    break
                    
        for j in d.values():
            res+=j[::-1]
        return res
"""
Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
"""