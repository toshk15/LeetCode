class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        res=0
        n=0
        for c in s:
            if c=="(":
                n+=1
                stack.append(c)
                res=max(res,n)
            elif c==")":
                n-=1
                stack.pop()
        return res
            
