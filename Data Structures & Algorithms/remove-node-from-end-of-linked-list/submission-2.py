# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_map: dict[int, ListNode] = {} # key: index, item: ListNode
        
        # first pass, create map and identify list length
        list_len = 0
        curr: ListNode = head
        while curr is not None:
            idx = list_len
            list_len += 1
            node_map[idx] = curr
            curr = curr.next

        idx_to_remove = list_len - n
        if idx_to_remove < 0:
            return head
        
        # handle valid removal
        if idx_to_remove == 0:
            head = head.next
        elif idx_to_remove == (list_len - 1):
            node_map[idx_to_remove-1].next = None
        else:
            prev_node = node_map[idx_to_remove - 1]
            next_node = node_map[idx_to_remove + 1]
            prev_node.next = next_node
        
        return head

        