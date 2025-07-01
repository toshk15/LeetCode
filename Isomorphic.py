def isIsomorphic(s1, s2):
    mapS1, mapS2 = {}, {}

    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]

        if ((c1 in mapS1 and mapS1[c1] != c2) or (c2 in mapS2 and mapS2[c2] != c1)):

            return False
        
        mapS1[c1] = c2
        mapS2[c2] = c1

    return True

s1 = "agg"
s2 = "fpp"

print(isIsomorphic(s1, s2))