class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(p):
            s=0
            for i in range(len(p)):
                if (i>0 and p[i-1]==10) or (i>1 and p[i-2]==10):
                    s+=2*p[i]
                else:
                    s+=p[i]
            return s
        p1=score(player1)
        p2=score(player2)
        if p1>p2:
            return 1
        if p2>p1:
            return 2
        return 0
            
