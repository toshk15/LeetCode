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

"""
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""