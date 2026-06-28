"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        copy_map: dict[Node, Node] = {}

        head_new = Node(head.val, None, None)
        head_old = head
        copy_map[head_old] = head_new

        # first pass, establish next pointers and copy map
        curr_old = head_old.next
        curr_new = head_new

        while curr_old != None:
            copy = Node(curr_old.val, None, None)
            curr_new.next = copy
            curr_new = copy
            # add new entry to map and proceed
            copy_map[curr_old] = curr_new
            curr_old = curr_old.next

        # second pass, add random pointers to new linked list
        curr_old = head_old
        curr_new = head_new
        while curr_old != None:
            if curr_old.random != None:
                curr_new.random = copy_map[curr_old.random]
            curr_old = curr_old.next
            curr_new = curr_new.next

        return head_new



        