def reverseStr(self, s: str, k: int) -> str:
    n=len(s)
    t=""
    for i in range(0,n,2*k):
        t+=s[i:i+k][::-1] 
        t+=s[i+k:i+2*k]
    return t            

s ="abcdefg"
#s ="hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
print(reverseStr(s,2))
