class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        for i in range(2,len(coordinates)):
            x3,y3=coordinates[i]
            if (x3-x2)*(y2-y1)!=(x2-x1)*(y3-y2):
                return False
            x2,y2=x3,y3
        return True
            
