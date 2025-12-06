class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        left=set()
        counter = Counter(s)

        for i in s:
            counter[i]-=1
            for ii in left:
                if counter[ii]>0:
                    res.add((i,ii))
            left.add(i)

        return len(res)


"""
Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

"""