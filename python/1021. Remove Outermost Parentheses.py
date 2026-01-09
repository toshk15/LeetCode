class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        c=0
        for n in s:
            if n=="(":
                if c>0:
                    stack.append("(")
                c+=1
            else:
                c-=1
                if c>0:
                    stack.append(")")
        return "".join(stack)
                
