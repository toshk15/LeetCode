class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def cycle(self, head):

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next

                return slow.val

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

print(head.cycle(head))


"""

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

"""