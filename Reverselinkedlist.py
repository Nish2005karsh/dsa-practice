# Reverse a linked list in python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next     # Save next
        curr.next = prev          # Reverse pointer
        prev = curr               # Move prev forward
        curr = next_node          # Move curr forward
    return prev
# next_node=curr.next
#curr.next=prev
# prev=curr
# curr=next_node