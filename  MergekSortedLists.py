import heapq
def mergeKLists(lists):
    heap=[]
    for i,node in enumerate(lists):
        if node:
            heapq.heappush(heap,(node.val,i,node))
    dummy=ListNode()
    curr=dummy

    while heap:
        val,i,node=heapq.heappop(heap)
        curr.next=node
        curr=node
        node=node.next
        if node:
            heapq.heappush(heap,(node.val,i,node))
    return dummy.next