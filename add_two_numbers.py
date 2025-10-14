class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def add_two_numbers(num1, num2):
    dummy = Node(0)
    curr = dummy

    carry = 0

    while num1 or num2 or carry:
        value1 = num1.data if num1 else 0
        value2 = num2.data if num2 else 0

        valueT = value1 + value2 + carry
        carry = valueT//10
        valueT = valueT%10
        curr.next = Node(valueT)

        curr = curr.next
        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None
    return dummy.next

"""
def addTwoNumbers(l1, l2):
    res = ListNode()
    resHead = res
    carry = 0
    while l1 and l2:
        new = ListNode(l1.val + l2.val + carry)
        carry = 0
        if new.val >= 10:
            carry = 1
            new.val -= 10
        l1, l2 = l1.next, l2.next
        res.next = new
        res = res.next
        
    cur = l1 if l1 else l2
    while cur:
        new = ListNode(cur.val + carry)
        carry = 0
        if new.val >= 10:
            carry = 1
            new.val -= 10
        cur = cur.next
        res.next = new
        res = res.next
    if carry:
        res.next = ListNode(1)
        
    return resHead.next
"""  
def printList(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
    
n1 = Node(9)
n1.next = Node(9)

n2 = Node(6)

res = add_two_numbers(n1,n2)
printList(res)



        
