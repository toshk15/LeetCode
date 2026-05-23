class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap=[]
        res=0
        for n in range(len(dist)):
            heapq.heappush(heap,dist[n]/speed[n])
        while heap:
            if res>=heapq.heappop(heap):
                return res
            res+=1
        return res
            
        
