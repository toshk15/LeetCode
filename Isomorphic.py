
"""
def isIsomorphic(s1, s2):
    mapS1, mapS2 = {}, {}

    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]

        if ((c1 in mapS1 and mapS1[c1] != c2) or (c2 in mapS2 and mapS2[c2] != c1)):

            return False
        
        mapS1[c1] = c2
        mapS2[c2] = c1

    return True
"""
def isIsomorphic(s,t):
    s_t = {}
    t_s = {}        
    for i in range(len(s)):
        if s[i] not in s_t:
            s_t[s[i]] = i
        if t[i] not in t_s:
            t_s[t[i]] = i
        if s_t[s[i]] != t_s[t[i]]:
            return False
    return True

s1 = "agg"
s2 = "fpp"

print(isIsomorphic(s1, s2))