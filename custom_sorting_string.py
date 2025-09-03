def customSorting(order, s):
    c = {}
    for i in s:
        c[i] = c.get(i,0) + 1

    res =""
    for x in order:
        if x in c:
            res += x * c[x]
            del c[x]
    for key, val in c.items():
        res += key * val
    
    return res


order = "abc"
s = "abcdabcG"
print(customSorting(order, s))

