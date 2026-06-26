from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check for null root
        if root is None:
            return []
        
        # Start queue for level order traversal, and put root on
        queue = deque([(root, 0)])
        level_order = []

        # Perform BFS search
        while len(queue) > 0:
            curr, n = queue.popleft()
            if n >= len(level_order):
                level_order.append([curr.val])
            else:
                level_order[n].append(curr.val)

            if curr.left is not None:
                queue.append((curr.left, n+1))
            if curr.right is not None:
                queue.append((curr.right, n+1))

        return level_order

        