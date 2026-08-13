class Solution:
    def calculate(self, s: str) -> int:
        nums=set("0123456789")
        ope=set("+*/-")
        stack=[]
        cur=0
        op="+"
        for idx in range(len(s)):
            if s[idx] in nums:
                cur = cur*10 + int(s[idx])
            if s[idx] in ope or idx==len(s)-1:
                if op == "+":
                    stack.append(cur)
                if op =="-":
                    stack.append(-cur)
                if op =="*":
                    stack[-1]*=cur
                if op =="/":
                    stack[-1]=int(stack[-1]/cur)
                cur=0
                op=s[idx]
        return sum(stack)
                
            
