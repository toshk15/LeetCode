class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head and not head.next:
            return head   
        left,right = self.middle(head)
        return self.merge(self.sortList(left), self.sortList(right))    

    def middle(self, head):
        slow = head
        fast = head.next               

        while fast and fast.next:         
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid
            
    def merge(self,l1,l2):
        dummy=ListNode(0,head)        
        curr=dummy

        while left or right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
            
        if left:
            curr.next = left
        if right:
            curr.next = right
           
        return dummy.next
            
   
    
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


s = Solution()
s.sortList(head)
#Solution.print_linked_list(sorted_head)
"""
def sortList(head):
    if not head or not head.next:
        return head

    # Step 1: Split the list into halves
    def split(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    # Step 2: Merge two sorted lists
    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    left, right = split(head)
    return merge(sortList(left), sortList(right))

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

"""
