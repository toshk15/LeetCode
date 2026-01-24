class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for l in logs:
            if stack and l=='../':
                stack.pop()
            elif l!='./':
                if l=='../':
                    continue
                else:
                    stack.append(l)
        return len(stack)
