# node class:
class Node:
    def __init__(self, val):
        self.next = None
        self.data = val

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return False  # No loop possible
        
        slow = head
        fast = head
        
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop found
                break
        else:
            return False  # No loop
        
        # Step 2: Find start of loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 3: Remove the loop
        ptr = slow
        while ptr.next != slow:
            ptr = ptr.next
        ptr.next = None
        
        return True  # Loop removed
