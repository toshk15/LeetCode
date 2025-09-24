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
