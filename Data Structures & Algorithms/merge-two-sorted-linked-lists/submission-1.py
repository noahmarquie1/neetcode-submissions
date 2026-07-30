# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # trivial base case
        if list1 == None and list2 == None:
            return None

        # Recursion step, adding next item
        node_val = 0
        if list1 == None:
            node_val = list2.val
            list2 = list2.next
        elif list2 == None:
            node_val = list1.val
            list1 = list1.next
        elif list1.val < list2.val:
            node_val = list1.val
            list1 = list1.next
        else:
            node_val = list2.val
            list2 = list2.next

        return ListNode(node_val, self.mergeTwoLists(list1, list2))

        