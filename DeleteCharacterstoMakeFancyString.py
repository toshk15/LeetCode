class Solution:
    def makeFancyString(self, s: str) -> str:
        ns=""
        for i in range(len(s)):
            if len(ns)>=2 and ns[-1]==s[i] and ns[-2]==s[i]:
                continue
            ns+=s[i]         
                
        return ns     
    
"""
Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".


"""