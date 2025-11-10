

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

s = "abcdefg"
t = "bagdecf"

print(isAnagram(s,t))

"""

def isAnagram(s, t):
    return sorted(s) == sorted(t)

s = "abcdefg"
t = "bagdecf"

print(isAnagram(s,t))
"""

"""
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""