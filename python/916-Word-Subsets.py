from collections import Counter
from collections import defaultdict

def wordSubsets(words1,words2):
    d={}     
    for w in words2:
        c2 = Counter(w)
        for i,j in c2.items():
            d[i]=max(d.get(i,0),j)
        
    res=[]
    for w in words1:
        c1 = Counter(w)
        f=True
        for ch,cnt in d.items():
            if c1[ch]<cnt:
                f=False
                break
        if f:
            res.append(w)
    return res




words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"]
words2 = ["c","cc","b"]

print(wordSubsets(words1, words2))


"""


Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

Output: ["leetcode"]

Example 3:

Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

Output: ["cccbb"]

"""