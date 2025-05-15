class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # node is the node to delete
    if node is None or node.next is None:
        # Can't delete if it's the last node using this method
        return
    
    # Copy value from next node
    node.val = node.next.val
    # Bypass the next node
    node.next = node.next.next
