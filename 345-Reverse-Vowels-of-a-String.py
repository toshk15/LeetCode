def reverseVowels(s):
    s=list(s)
    l=0
    r=len(s)-1
    vowels={'a','e','i','o','u', 'A','E','I','O','U'}       

    while l<r:
        if s[l] not in vowels:
            l+=1
        elif s[r] not in vowels:
            r-=1
        if s[l] in vowels and s[r] in vowels:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
    return "".join(s)
"""

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

"""