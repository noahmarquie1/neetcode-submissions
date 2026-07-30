# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Look through linked list recursively
        # At each step, set curr.next to end, and end.next to old curr.next,
        #   then do recursion on old curr.next
        # Edge cases are:
        #  1. head == None - should return None
        #  2. list length == 1 - return head 
        
        if head == None or head.next == None or head.next.next == None:
            return

        # Find next and last items
        next_item = head.next
        
        # Find last item (unfortunately will take a while each time!)
        # Make sure to cut it off from list by tracking trailing item
        last_item = head.next
        trailing = head
        found_last = False
        while not found_last:
            if last_item.next == None:
                found_last = True
            else:
                last_item = last_item.next
                trailing = trailing.next

        trailing.next = None

        head.next = last_item
        last_item.next = next_item
        self.reorderList(next_item)

        

        
        