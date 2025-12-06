class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        c=0
        for ch in word:
            if ch.lower() in s and ch.upper() in s:
                c+=1
                s.remove(ch.lower())
                s.remove(ch.upper())
        return c
    
"""
Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.


"""