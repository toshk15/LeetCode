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



class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            value = min(self.minStack[-1],val)
        else:
            value = val
        self.minStack.append(value)

    def pop(self) -> None:      
        self.stack.pop()
        if self.minStack:
            self.minStack.pop()             

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        
s= MinStack()
s.push(-2)
s.push(0)
s.push(-1)
print(s.getMin())
s.pop()
print(s.getMin())

"""
def largestTriangleArea(points):
    maxi=float("-inf")
    maxj=float("-inf")
    for i,j in points:
        if i>maxi:
            maxi=i
        if j>maxj:
            maxj=j
    area=(maxi*maxj)/2
    return area

points = [[1,0],[0,0],[0,1]]
print(largestTriangleArea(points))
