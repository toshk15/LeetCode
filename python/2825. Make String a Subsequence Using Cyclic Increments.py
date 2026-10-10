class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=0
        for c in str1:
            nxt_c="a" if c=="z" else chr(ord(c)+1)
            if i<len(str2) and str2[i] in (c,nxt_c):
                i+=1
        return i==len(str2)
