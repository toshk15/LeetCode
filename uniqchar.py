from collections import Counter

def fistUniqChar(s):
    c = Counter(s)
    for key, value in c.items():
        if value==1:
            return s.index(key)
    return -1

s = "aabcdtbcd"
print(fistUniqChar(s))

