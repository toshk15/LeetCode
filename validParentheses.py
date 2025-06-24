def isValidPare(s):
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

s = "}{()"
print(isValidPare(s))