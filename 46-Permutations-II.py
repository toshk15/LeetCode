def permutation(s, sel,res, k):
    n = len(s)
    if k == n:
        print(res)
        return
    
    for i in range(n):
        if sel[i] == False:
            if k>0 and (ord(s[i]) - ord(res[k-1])) == 1:
                continue

            res[k] = s[i]
            sel[i] = True
            permutation(s, sel, res, k+1)
            sel[i] = False
    
s = ["a","b","c"]
sel = [False, False, False]
k=0
res = [0,0,0]
permutation(s,sel,res, k)
