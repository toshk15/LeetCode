from collections import Counter
def frequencySort(s):
    c = Counter(s)
    res=[]
    c=sorted(c.items(), key=lambda item: item[1], reverse=True)
       
    for key, value in c:
        res.append(key*value)
    return "".join(res)

s ="tree"