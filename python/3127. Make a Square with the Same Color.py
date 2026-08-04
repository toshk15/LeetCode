class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            w=0
            b=0
            for j in range(2):
                if grid[i][j]=="B":
                    b+=1
                else:
                    w+=1
                if grid[i+1][j]=="B":
                    b+=1
                else:
                    w+=1
            if w>=3 or b>=3:
                return True
            w=0
            b=0
            for j in range(1,3):
                if grid[i][j]=="B":
                    b+=1
                else:
                    w+=1
                if grid[i+1][j]=="B":
                    b+=1
                else:
                    w+=1
            if w>=3 or b>=3:
                return True
        return False
                
                    
                    
