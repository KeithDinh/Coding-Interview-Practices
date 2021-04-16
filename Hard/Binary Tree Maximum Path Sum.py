# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        maxPath = float('-inf')
    
        def traverseSave(current):
            if not current:
                return 0
            
            nonlocal maxPath
            
            left = max(traverseSave(current.left),0)
            
            right = max(traverseSave(current.right),0)
            
            maxPath = max(maxPath, current.val + left + right)
            
            return current.val + max(left,right)
        
        traverseSave(root)
        
        return maxPath