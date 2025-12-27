class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-i for i in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            val= -heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(sqrt(val)))
        return -sum(gifts)
        
