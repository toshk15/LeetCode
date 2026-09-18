class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sig=1
        i=0
        if len(s)==0:
            return 0
        if len(s)==1 and not s[i].isdigit():
            return 0
        if s[i]=="+":
            sig=1
            i+=1
        if s[i]=="-":
            sig=-1
            i+=1
        if i==2:
            return 0
        val=0
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                val=val*10+ int(s[i])
            i+=1
        val=val*sig
        if val <= -2**31-1:
            return -2**31
        elif val>2**31-1:
            return 2**31-1
        else:
            return val
        
        
