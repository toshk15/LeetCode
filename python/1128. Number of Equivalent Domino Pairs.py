class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c=defaultdict(int)
        s=0
        for x,y in dominoes:
           if y>x:
              x,y=y,x
           c[(x,y)]+=1
        for v in c.values():
           s+=v*(v-1)//2
        return s
                
