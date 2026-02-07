class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d={chr(j):str(i) for i,j in enumerate(range(ord("a"),ord("j")+1))}
        f=""
        s=""
        t=""
        for i in firstWord:
            f+=d[i]
        for i in secondWord:
            s+=d[i]
        for i in targetWord:
            t+=d[i]
        return int(t)==(int(f)+int(s))
