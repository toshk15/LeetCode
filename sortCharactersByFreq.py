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
    
s = "fererr"

print(freqCharSort(s))