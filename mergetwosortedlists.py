class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()  # Dummy node to ease operations
    tail = dummy # Tail pointer to keep track of the merged list
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # Append the remaining nodes
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

# Example usage
# 