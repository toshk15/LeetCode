class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a", "e", "i", "o", "u"}
        l=0
        res=0
        c=0

        for r in range(len(s)):
            if s[r] in vowels:
                c+=1          
           
            if r-l+1 > k:
                if s[l] in vowels:
                    c-=1
              
                l+=1
            res = max(res, c)
        return res
    
"""
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

"""