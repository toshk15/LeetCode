from collections import Counter
from collections import defaultdict

def freqCharSort(s):
    count = Counter(s)
    buckets = defaultdict(list)

    for char, cnt in count.items():
        buckets[cnt].append(char)
    
    res = []
    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c*i)
    return "".join(res)


"""
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res=[]
        c=sorted(c.items(), key=lambda item: item[1], reverse=True)
       
        for key, value in c:
            res.append(key*value)
        return "".join(res)

"""
    
s = "fererr"

print(freqCharSort(s))

"""
Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""