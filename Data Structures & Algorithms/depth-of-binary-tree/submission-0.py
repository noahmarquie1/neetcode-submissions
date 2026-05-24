# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: # Base case
            return 0
        # Recursion step, each layer should add 1 to the count
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        