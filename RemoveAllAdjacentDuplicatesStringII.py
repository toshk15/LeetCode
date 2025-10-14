def removeDuplicates(s, k):

    stack = []

    for car in s:

        if stack and stack[-1][0] == car:
            stack[-1][1] += 1
        else:
            stack.append([car, 1])
        
        if stack[-1][1] == k:
            stack.pop()
    res = ""

    for c, count in stack:
        res += (c * count)

    return res

"""
def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = []

        for st in s:
            if stack and stack[-1] == st:
                count[-1] += 1
                if count[-1] == k:
                    stack.pop()
                    count.pop()
            else:
                stack.append(st)
                count.append(1)
            
        result = ""
        for i in range(len(stack)):
            result += (stack[i] * count[i])
        
        return result
"""

s = "aaaabbbad"
k = 2
print(removeDuplicates(s, k))