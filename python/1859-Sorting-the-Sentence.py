class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split()
        res=[0]*len(ss)
        for w in ss:
            idx = int(w[-1])-1
            res[idx]=w[0:-1]
        return " ".join(res)
    
"""
Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

"""