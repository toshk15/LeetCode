class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class LinkList:
    def __init__(self):
        self.head = None
"""
def MergeLinkList(l1, l2):

    aux = node = Node(0)

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 or l2
    return aux.next

def printMerge(curr):
    c = curr
    while c:
        print(c.val)
        c = c.next



l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(5)

l2 = Node(3)
l2.next = Node(3)
l2.next.next = Node(6)
l2.next.next.next = Node(8)
l2.next.next.next.next = Node(9)
curr = MergeLinkList(l1, l2)
printMerge(curr)


"""
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

        