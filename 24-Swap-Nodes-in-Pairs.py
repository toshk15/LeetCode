def swapPairs(head):
    if not head:
        return None     

    aux = ListNode(0, head)
    curr = head
    prev = aux

    while curr and curr.next:
        temp = curr.next.next
        second = curr.next

        curr.next = temp
        second.next = curr
        prev.next = second

        prev = curr
        curr = temp
            
    return aux.next
