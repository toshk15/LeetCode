class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        comb=[]
        res=[]

        def backtrack():
            if len(comb)==len(nums):
                res.append(comb[:])                
            
            for n in c:
                if c[n]==0:
                    continue
                comb.append(n)
                c[n]-=1

                backtrack()
                comb.pop()
                c[n]+=1
        backtrack()
        return res  
    

"""   
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
""" 