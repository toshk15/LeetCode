class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=set()
        comb=[]

        def bracktrack():
            if len(comb)==len(nums):
                res.append(comb[:])
                return
            
            for n in nums:
                if n not in used:
                    comb.append(n)
                    used.add(n)
                    bracktrack()
                    comb.pop()
                    used.remove(n)
        bracktrack()
        return res


"""

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

"""