def wordPattern(pattern, s):
    mp = {}
    ms = {}
    s=s.split()

    if len(s)!=len(pattern):
        return False
       
    for i, j in zip(pattern, s):
        if i in ms and ms[i]!=j:
            return False
        if j in mp and mp[j]!=i:
            return False
        mp[j]=i
        ms[i]=j

    return True

s = "dog cat cat dog"
pattern = "abba"