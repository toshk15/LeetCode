# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        points=[]
        maxx=0
        minn=float("inf")
        while head:
            arr.append(head.val)
            head=head.next
        for i in range(1,len(arr)-1):
            if arr[i-1]>arr[i]<arr[i+1] or arr[i-1]<arr[i]>arr[i+1]:
                points.append(i)
        if len(points)<2:
            return [-1,-1]
        maxx=points[-1]-points[0]
        for i in range(1,len(points)):
            minn=min(points[i]-points[i-1],minn)
        return [minn,maxx]
        
                
