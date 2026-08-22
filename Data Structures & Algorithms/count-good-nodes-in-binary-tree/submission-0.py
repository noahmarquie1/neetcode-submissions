# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.n_good = 0

    def searchTree(self, root, max_seen):
        if root == None:
            return 

        if root.val >= max_seen:
            self.n_good += 1
            max_seen = root.val

        self.searchTree(root.left, max_seen)
        self.searchTree(root.right, max_seen)
        


    def goodNodes(self, root: TreeNode) -> int:
        # use depth-first search, keeping track of what has been seen so far
        # Premise:
        #  1. at any point in tree, assume previous nodes are known
        #  2. call recursive function on children, adding current node to seen
        
        self.searchTree(root, root.val)
        return self.n_good


        