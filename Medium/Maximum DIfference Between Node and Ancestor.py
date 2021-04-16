# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        diff =[0]
        maxVal, minVal = self.findMaxMinSubTree(root, diff)
        
        diff[0] = max(diff[0], max(abs(root.val - maxVal), abs(root.val-minVal)))
        
        return diff[0]
        
    def findMaxMinSubTree(self, current: TreeNode, diff):
    
        if not current.left and not current.right:
            return (current.val, current.val)
        
        maxVal = minVal = 0
        if not current.left:
            maxVal, minVal = self.findMaxMinSubTree(current.right, diff)
            
        elif not current.right:
            maxVal, minVal = self.findMaxMinSubTree(current.left, diff)

        else:
            maxVal1, minVal1 = self.findMaxMinSubTree(current.left, diff)
            maxVal2, minVal2 = self.findMaxMinSubTree(current.right, diff)
            maxVal = max(maxVal1, maxVal2)
            minVal = min(minVal1, minVal2)
        
        diff[0] = max(diff[0], max(abs(current.val - maxVal), abs(current.val-minVal)))
        return (max(maxVal, current.val), min(minVal, current.val))