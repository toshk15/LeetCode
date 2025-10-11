def reverseStr(s,k):
    i=0
    n=len(s)
    t=""
    while k*i < n:
        t+=s[2*k*i:2*k*(i+1)][::-1]
        t+=s[2*k*(i+1):2*2*k*(i+1)]            
        #print(t)
        i+=1
        
    return t
s ="abcdefg"
#s ="hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
print(reverseStr(s,2))
