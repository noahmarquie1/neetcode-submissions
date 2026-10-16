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

        left_valid = self.isValidBST(root.left)
        curr_valid = root.val > self.max_seen
        self.max_seen = root.val

        return (
            left_valid and 
            curr_valid and 
            self.isValidBST(root.right)
        )
        




        