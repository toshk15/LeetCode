def removeNthFromEnd(head,n):
    right = head        
    aux = ListNode(0,head)
    left = aux      

    while n>0:
        right = right.next
        n-=1
        
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
       
    return aux.next