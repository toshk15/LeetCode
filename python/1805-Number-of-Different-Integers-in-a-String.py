class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        d=""
        s=set()
        for c in range(len(word)):
            if word[c].isdigit():
                d+=word[c]
            if d and not word[c].isdigit():
                s.add(int(d))
                d=""
            if d and c==len(word)-1:
                s.add(int(d))
        return len(s)
"""
Example 1:

Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

Example 2:

Input: word = "leet1234code234"
Output: 2

Example 3:

Input: word = "a1b01c001"
Output: 1
Explanation: The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.

"""