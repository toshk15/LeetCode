"""
def reverse(s):
    s = list(s)

    l, r = 0, len(s) - 1 
    
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s 
s = "fernando"
print(reverse(s))

"""
def reverse(s):

    stack = []
    res = []
    for i in s:
        stack.append(i)
    while stack:
        res.append(stack.pop())
    res = ''.join(res)
    return res

s = "fernando"
print(reverse(s))

 