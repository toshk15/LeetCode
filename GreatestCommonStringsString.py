"""
def greatesCommonDivisorStrings(s1, s2):
    def option(pattern, target):
        sp = ""
        while len(sp) < len(target):
            sp+=pattern

        return sp == target
    
    for lenght in range(min(len(s1), len(s2)), 0, -1):
        sp = s1[:lenght]

        if option(sp, s1) and option(sp, s2):
            return sp
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


#s1 = "ABABAB"
#s2 = "ABAB"

s1 = "ABCABC"
s2 = "ABCR"

print(greatesCommonDivisorStrings(s1,s2))
