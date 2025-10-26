def remove_stars(s):
    stack = []

    for x in s:
        if x == "*":
            stack and stack.pop()
        else:
            stack.append(x)
    return "".join(stack)

s = "abc**abc**"
print(remove_stars(s))