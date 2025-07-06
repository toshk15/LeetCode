def lenghtLogestSubString(s):
    cSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in cSet:
            cSet.remove(s[l])
            l += 1
        cSet.add(s[r])
        res = max(res, r - l +1)
    return res

s = "abcabcd"
print(lenghtLogestSubString(s))


"""
s = set()
s.add("a")
s.add("b")
s.add("c")
print(s)
s.remove()
"""