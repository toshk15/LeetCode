def mergeStringsAlter(s1, s2):

    i, j = 0, 0
    res = []
    while i < len(s1) and j < len(s2):
        res.append(s1[i])
        res.append(s2[j])
        i+=1
        j+=1
    res.append(s1[i:])
    res.append(s2[j:])
    return "".join(res)

s1 = "aceg"
s2 = "bdfh"

print(mergeStringsAlter(s1, s2))