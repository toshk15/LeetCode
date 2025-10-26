def encode(strs):
    res =""
    for s in strs:
        res += str(len(s))+"#"+s
    return res

def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j+=1
        lenS = int(s[i:j])
        i = j + 1
        j = i + lenS
        res.append(s[i:j])
        i = j
    return "".join(res)

strs = "leet code"
se = encode(strs)
print(se)
print(decode(se))
