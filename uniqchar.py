def fistUniqChar(s):
    count_char = {}

    for c in s:
        count_char[c] = 1 + count_char.get(c,0)
    
    for i, c in enumerate(s):
        if count_char[c] == 1:
            return i
    return -1

s = "aabcdtbcd"
print(fistUniqChar(s))

