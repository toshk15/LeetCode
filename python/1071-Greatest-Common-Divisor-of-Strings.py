class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1=len(str1)
        s2=len(str2)
        ss=""

        def common(s,target):
            ns=""
            while len(ns)<len(target):
                ns+=s
            return ns==target

        for i in range(min(s1,s2),0,-1):
            ss=str1[:i]

            if common(ss,str1) and common(ss,str2):
                return ss
        return ""
    
"""
def greatesCommonDivisorStrings(s1, s2):
    len1, len2 = len(s1), len(s2)

    def isDivisor(s):
        if len1%s or len2%s:
            return False
    
        f1, f2 = len1//s, len2//s
        return s1[:s] * f1 == s1 and s1[:s] * f2 == s2
    
    for s in range(min(len1, len2), 0, -1):
        if isDivisor(s):
            return s1[:s]
    return ""
"""

"""

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""