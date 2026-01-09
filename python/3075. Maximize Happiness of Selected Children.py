class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness=[-n for n in happiness]
        heapq.heapify(happiness)
        item=0
        sumhappy=0

        for i in range(k):
            x=-heapq.heappop(happiness)
            sumhappy+=max(x-item,0)
            item+=1
        return sumhappy
        
