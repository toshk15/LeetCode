class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for n in operations:
            if n!="C" and n!="D" and n!="+":
                stack.append(int(n))
            elif n=="+":
                res=0
                res=stack[-1]+stack[-2]
                stack.append(int(res))
            elif n=="D":
                res=stack[-1]*2
                stack.append(res)
            elif n=="C":
                stack.pop()
        return sum(stack)
