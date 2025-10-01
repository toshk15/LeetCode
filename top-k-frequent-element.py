"""
def topKFrequent(nums, k):
    counter = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        counter[n] = 1 + counter.get(n,0)
    for n, c in counter.items():
        freq[c].append(n)

    res=[]
    for i in range(len(freq)-1, 0,-1):
        res+=freq[i]
        if len(res)==k:
            return res
"""
from collections import Counter

def topKFrequent(nums, k):
    d = Counter(nums)
    maxval = max(d.values()) 
    res=[]
    bucket=[[] for i in range(maxval+1)]
              
    for key, values in d.items():
        bucket[values].append(key)
    for i in range(len(bucket)-1,0,-1):
        res+=bucket[i]
        if len(res) == k:
            return res
            
nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))