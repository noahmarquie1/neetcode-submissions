# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: # base case
            return None
        if head.next == None:
            return head
        
        curr = head
        prev = head
        while curr.next != None:
            prev = curr
            curr = curr.next
        
        prev.next = None
        curr.next = self.reverseList(head)
        return curr
        