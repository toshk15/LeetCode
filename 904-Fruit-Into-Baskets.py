class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c=defaultdict(int)
        l=0
        res=0
        for r in range(len(fruits)):
            c[fruits[r]]+=1
            if len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    c.pop(fruits[l])
                l+=1
            res=max(r-l+1, res)
        return res
        
"""
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

"""