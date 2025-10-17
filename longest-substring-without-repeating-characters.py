"""
def lengthOfLongestSubstring(s):
    charSet = set()
    l=0
    res=0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res=max(res, r-l+1)
    return res

def lengthOfLongestSubstring(s):
    l = 0
    hs = set()
    ans = 0
    for r, ch in enumerate(s):
        while ch in hs:
            hs.remove(s[l])
            l += 1
        hs.add(ch)
        ans = max(ans, r-l+1)

    return ans

"""
def lengthOfLongestSubstring(s):
    b=0
    for i in range(len(s)):
        a=s[i]
        for j in range(i+1,len(s)):
            if s[j] not in a: 
                a+=s[j]
            else: 
                break
        if b<len(a): 
            b=len(a)
    return b

s="pwwkew"

#s="xxxx"
print(lengthOfLongestSubstring(s))



