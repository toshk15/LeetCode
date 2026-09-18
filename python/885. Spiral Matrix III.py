class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        res=[[rStart,cStart]]
        steps=1
        size=cols*rows
        if size==1:
            return res
        rS=rStart
        cS=cStart
        while True:
            dir=[(0,1,steps),(1,0,steps),(0,-1,steps+1),(-1,0,steps+1)]
            for dr,dc,st in dir:
                for x in range(st):
                    rS+=dr
                    cS+=dc
                    if 0<=rS<rows and 0<=cS<cols:
                        res.append([rS,cS])
                        if len(res)==size:
                            return res
            steps+=2
            
            
            
