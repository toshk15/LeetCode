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