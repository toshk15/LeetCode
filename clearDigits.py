def clearDigits(s):
    res = []
    delete_c = 0

    def isdigit(c):
        return ord("0") <= ord(c) <= ord("9")
    

    for i in reversed(range(len(s))):
        if isdigit(s[i]):
            delete_c += 1
        elif delete_c:
            delete_c -= 1
        else:
            res.append(s[i])
    return "".join(res[::-1])

#s = "abcd23"
#s = "23de"
s = "23de9"
print(clearDigits(s))