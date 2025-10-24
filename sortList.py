class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def sortList(self, head):
        if not head or not head.next:
            return head 

        mid=self.middle(head)
        left=self.sortList(head)
        right=self.sortList(mid)

        return self.merge(left, right)

    def merge(self,l1,l2):
        dummy=ListNode()        
        curr=dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next
        

    def middle(self,head):
        slow=head
        fast=head.next

        while fast and fast.next:
            slow =slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None        
        return mid           
   
    
    def print_linked_list(self,head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

head = ListNode(10)
head.next = ListNode(2)
head.next.next = ListNode(7)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(9)

newhead=head.sortList(head)
head.print_linked_list(newhead)
