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


s = "aaaabbbad"
k = 2
print(removeDuplicates(s, k))