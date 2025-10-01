from collections import Counter
def repeatedCharacter(s):
        """
        c = Counter(s)
        print(c)
        d = set(s)
        d=list(d)
        d.sort()
        res=0
        smin=""
        idmin=float('inf')
        for i in d:            
            if c[i]>=2:
                id1 = s.find(i)
                id2 = s.find(i,id1+1)
                res = id2-id1               
                idmin = min(idmin, res)
                smin=i
        return smin
        """
       
        f = set()

        for i in s:
            if i in f:
                return i
            f.add(i)
s = "abccbaacz"
print(repeatedCharacter(s))