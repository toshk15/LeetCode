from collections import Counter
def findTheDifference(s, t):
    c=Counter(s)
    cc=Counter(t)
    res=[]
    common=set(t)
    for i in common:
        r=cc.get(i,0)-c.get(i,0)
        if r==0:
            continue
        else:
            res.append(r*i)
    return "".join(res)
      

s = "abcd"
t = "abcde"