class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumapple=sum(apple)
        capacity=[-n for n in capacity]
        heapq.heapify(capacity)
        ap=0
        while sumapple>0:
            sumapple-=(-heapq.heappop(capacity))
            ap+=1
        return ap
        
