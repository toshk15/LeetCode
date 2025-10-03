"""
def isValid(s):
    stack = []
    parentheses = { ")":"(", "]":"[", "}":"{" }

    for c in s:
        if c in parentheses:
            if stack and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False
"""
def isValid(s):
    stack=[]

    if len(s)==1:
        return False

    for c in s:
        if c=="(":
            stack.append(")")
        elif c=="{":
            stack.append("}")
        elif c=="[":
            stack.append("]")
        else:
            if not stack:
                return False
            cc=stack.pop()
            if c!=cc:
                return False
    if stack:
        return False
    return True
        

s = "()"
print(isValid(s))