class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        ditochar={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"qprs","8":"tuv","9":"wxyz"}

        def backtrack(i,strr):
            if len(strr)==len(digits):
                res.append(strr)
                return
            
            for c in ditochar[digits[i]]:
                #strr=strr+c
                backtrack(i+1,strr+c)
        if digits:
            backtrack(0,"")
        return res
    
"""

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "2"
Output: ["a","b","c"]

"""