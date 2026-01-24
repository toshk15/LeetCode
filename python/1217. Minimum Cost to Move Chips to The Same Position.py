class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even=0
        odd=0
        for n in position:
            if n%2:
                odd+=1
            else:
                even+=1
        return min(odd,even)
            
        
