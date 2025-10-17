def longestCommonPrefix(strs):
    mi = min(strs)
    ma = max(strs)
    s=""
    for i in range(len(mi)):
        if mi[i]==ma[i]:
            s+=mi[i]
        else:
            break
    return s

strs = ["flower","flow","flight"]