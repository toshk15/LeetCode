class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        if len(s)<8:
            return False
        stack=[]
        upper=1
        lower=1
        digit=1
        spe=1
        specials="!@#$%^&*()-+"
        for c in range(len(s)):
            if c<len(s)-1 and s[c]==s[c+1]:
                return False
            if s[c].isupper() and upper==1:
                stack.append(1)
                upper=0
            elif s[c].islower() and lower==1:
                stack.append(1)
                lower=0
            elif s[c].isdigit() and digit==1:
                stack.append(1)
                digit=0
            elif s[c] in specials and spe==1:
                stack.append(1)
                spe=0
        print(stack)
        return True if len(stack)==4 else False
        
        
