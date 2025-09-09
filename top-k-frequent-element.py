def topFreqElement(nums, k):
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
        
nums = [1,1,1,2,3,3,4]
k = 2

print(topFreqElement(nums, k))