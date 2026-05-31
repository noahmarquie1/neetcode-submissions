# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def containsNode(self, root: TreeNode, node: TreeNode):
        if root is None:
            return False
        elif root.val == node.val:
            return True
        else:
            return self.containsNode(root.left, node) or self.containsNode(root.right, node)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        elif (self.containsNode(root.left, p) and self.containsNode(root.left, q)):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (self.containsNode(root.right, p) and self.containsNode(root.right, q)):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        