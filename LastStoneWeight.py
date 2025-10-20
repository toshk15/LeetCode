import heapq

def lastStoneWeight(stones):
  
  
    max_stones = [-n for n in stones]  
    heapq.heapify(max_stones) 
    print(max_stones)

    while len(max_stones)>1:
        largest = heapq.heappop(max_stones)
        next_largest = heapq.heappop(max_stones)
        
        if largest != next_largest:
            heapq.heappush(max_stones, largest-next_largest)
        
    if len(max_stones)==1:
        return -heapq.heappop(max_stones)
    else:
        return 0
    
    """
    stones.sort()
    while len(stones)>1:
        largest = stones.pop()
        next_largest = stones.pop()

        if largest != next_largest:
            x=largest-next_largest
            stones.append(x)
    if len(stones)==1:
        return stones.pop()
    else:
        return 0

  """
   
#stones=[1,1,1]
stones= [2,7,4,1,8,1]
print(lastStoneWeight(stones))
