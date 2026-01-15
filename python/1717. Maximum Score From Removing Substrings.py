class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_prio="ab"
        low_prio="ba"

        if x<y:
            x,y=y,x
            max_prio, low_prio=low_prio,max_prio

        stack=[]
        sum_total=0
        for i in s:
            if i==max_prio[1] and stack and stack[-1]==max_prio[0]:
                stack.pop()
                sum_total+=x
            else:
                stack.append(i)
        stack_low=[]
        for i in stack:
            if i==low_prio[1] and stack_low and stack_low[-1]==low_prio[0]:
                stack_low.pop()
                sum_total+=y
            else:
                stack_low.append(i)   
        return sum_total 
