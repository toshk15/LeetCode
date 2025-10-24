from collections import Counter
def canConstruct(ransomNote, magazine):
    m=Counter(magazine)
    r=Counter(ransomNote)

    for i,j in r.items():
        if i in m:
            if m[i]>=j:
                continue
            else:
                return False  
        else:
            return False
    return True


"""
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""