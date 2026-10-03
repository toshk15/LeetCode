class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res=0
        for f in fruits:
            for b in range(len(baskets)):
                if f<=baskets[b]:
                    baskets[b]=-1
                    break
                
        return len(baskets)-baskets.count(-1)
                    
