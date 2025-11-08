class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        maxOdd = 0
        maxEven=float("inf")

        for j in c.values():
            if j%2==1:
                if maxOdd<j:
                    maxOdd=j
            if j%2==0:
                if maxEven>j:
                    maxEven=j
        return maxOdd-maxEven
        
"""

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

    The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
    The maximum difference is 5 - 2 = 3.

Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

    The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
    The maximum difference is 3 - 2 = 1.


"""