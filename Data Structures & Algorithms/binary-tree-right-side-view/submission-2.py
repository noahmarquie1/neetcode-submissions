# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do a level order traversal, only add to list when next node is in next level

        curr = (root, 0)
        right_visible = []
        queue = []
        # queue is to be formed as tuples with (node, level)

        while curr[0] != None:
            if curr[0].left != None:
                queue.append((curr[0].left, curr[1] + 1))
            if curr[0].right != None:
                queue.append((curr[0].right, curr[1] + 1))

            if len(queue) > 0:
                if queue[0][1] > curr[1]:
                    right_visible.append(curr[0].val)
                curr = queue[0]
                queue.pop(0)
            else:
                right_visible.append(curr[0].val)
                curr = (None, None)

        return right_visible