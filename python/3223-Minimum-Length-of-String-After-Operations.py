from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        res=0
        c = Counter(s)

        for i in c.values():
            if i%2==0:
                res+=2
            else:
                res+=1        
        return res
"""
Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

    Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
    Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".

Example 2:

Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.
"""