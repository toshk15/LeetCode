class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        COL=len(board[0])
        ROW=len(board)
        board[rMove][cMove]=color
        dir=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        def valid(r,c,color,dir):
            dr,dc=dir
            r=r+dr
            c=c+dc
            lg=1
            while 0<=r<ROW and 0<=c<COL:
                lg+=1
                if board[r][c]==".":
                    return False
                elif board[r][c]==color:
                    return lg>=3
                r=r+dr
                c=c+dc
            return False
        for d in dir:
            if valid(rMove,cMove,color,d):
                return True
        return False
                
