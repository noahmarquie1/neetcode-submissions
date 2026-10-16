# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_seen = -1000000001

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False
        if root.val <= self.max_seen:
            return False

        self.max_seen = root.val
        return self.isValidBST(root.right)
        




        