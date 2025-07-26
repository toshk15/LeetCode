def partitionString(s):
    string_set = set()
    res = 1

    for c in s:
        if c in string_set:
            res += 1
            string_set = set()
        string_set.add(c)
    return res

s = "abcab"
print(partitionString(s))