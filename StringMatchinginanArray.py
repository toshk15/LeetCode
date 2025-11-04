class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in words:
            for j in words:
                if i==j:
                    continue
                if i in j:
                    if i not in res:
                        res.append(i)
        return res
    
"""
Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

"""