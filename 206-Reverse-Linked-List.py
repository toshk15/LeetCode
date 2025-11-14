def reverseList(head):
    prev= None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr=temp

    return prev

"""
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

"""