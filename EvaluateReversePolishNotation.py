class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        if len(tokens)==1:
            return int(tokens[0])
        for n in tokens:
            if n not in ['+','-','*','/']:
                stack.append(n)
            elif n=="+":
                x1=int(stack.pop())
                x2=int(stack.pop())
                res= x2+x1
                stack.append(res)
            elif n=="-":
                x1=int(stack.pop())
                x2=int(stack.pop())
                res= x2-x1
                stack.append(res)
            elif n=="*":
                x1=int(stack.pop())
                x2=int(stack.pop())
                res= x2*x1
                stack.append(res)
            elif n=="/":
                x1=int(stack.pop())
                x2=int(stack.pop())
                res=int(x2/x1)             
                stack.append(res)
        return res
    
    
""" 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""