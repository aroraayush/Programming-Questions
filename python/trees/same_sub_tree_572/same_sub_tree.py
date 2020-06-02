# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if s == None and t == None:
            return True
        elif s == None or t == None:
            return False
        
        # Applying the subtree to every tree node of main tree
        
        if self.is_same(s, t):
            return True
        elif self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False
        
    def is_same(self, s : TreeNode, t: TreeNode) -> bool:
        # Base case: empty tree
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False

        # Recursive case : Solve the smallest tree
        # Use solution of smaller tree to solve larger tree
        # Pre-oder : Do operation, check left, check right

        if s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right) :
            return True
        
        return False
    
    
        