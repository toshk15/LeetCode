class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
        if len(word)<3:
            return False

        for n in word.lower():
            if n in "aeiou":
                v+=1
            elif not n.isdigit() and not n.isalpha():
                return False
            elif n.isalpha():
                c+=1
        if c>=1 and v>=1:
            return True
        else:
            return False
        
"""

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.
"""