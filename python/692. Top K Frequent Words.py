class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c=Counter(words)
        heap=[]
        res=[]
        for w,f in c.items():
            heapq.heappush(heap,(-f,w))
        for i in range(k):
            freq,word=heapq.heappop(heap)
            res.append(word)
        return res
            
            
