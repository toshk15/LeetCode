class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries=sorted([(q,i) for i,q in enumerate(queries)])
        j=0
        maxx=0
        res=[0]*len(queries)
        for q,i in queries:
            while j<len(items) and items[j][0]<=q:
                maxx = max(maxx,items[j][1])
                j+=1
            res[i]=maxx
        return res
    
            
        
