# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode(0)
        done = False
        curr = sum

        while not done:
            if l1 is None and l2 is None:
                done = True
                break

            node_val = curr.val
            if l1 is not None:
                node_val += l1.val
                l1 = l1.next
            if l2 is not None:
                node_val += l2.val
                l2 = l2.next

            first_digit_val = node_val % 10
            second_digit_val = int(node_val / 10)
            curr.val = first_digit_val

            if second_digit_val > 0:
                curr.next = ListNode(second_digit_val)
                curr = curr.next
            elif l1 is not None or l2 is not None:
                curr.next = ListNode(0)
                curr = curr.next

        return sum


        