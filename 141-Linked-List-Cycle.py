class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def cycle(self, head):

        p, q = head, head

        while q and q.next:
            p = p.next
            q = q.next.next

            if p == q:
                return True
        return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

print(head.cycle(head))

