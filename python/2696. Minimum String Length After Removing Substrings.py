class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for c in s:
            if stack:
                if stack[-1]+c=="AB" or stack[-1]+c=="CD":
                    stack.pop()
                    continue
        
            stack.append(c)
        return len(stack)
