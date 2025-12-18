class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            ss = set()
            for j in range(i, n):
                ss.add(s[j])
               
                is_nice = True
                for char in ss:
                    if char.lower() not in ss or char.upper() not in ss:
                        is_nice = False
                        break
               
                if is_nice and len(s[i:j+1]) > len(res):
                    res = s[i:j+1]
        return res
    
"""
Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

"""