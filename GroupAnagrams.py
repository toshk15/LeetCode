from collections import Counter
def groupAnagrams(strs):
    G={}
        
    for i in strs:
        c=Counter(i)
        
        t = tuple(sorted(c.items()))
        if t in G:
            G[t].append(i)
        else:
            G[t]=[i]
    return list(G.values())


strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))