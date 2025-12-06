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
print(wordPattern(pattern,s))


"""

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

"""