# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d = dict()
        self.findSumByLevel(root, 0, d)
        m = max(d.values())
        for i in d.keys():
            if d[i] == m:
                return i+1
        return None
        
    def findSumByLevel(self, node, level, d):
        if node:
            if level in d.keys():
                d[level] += node.val
            else:
                d[level] = node.val
            
            self.findSumByLevel(node.left, level+1, d)
            self.findSumByLevel(node.right, level+1, d)
        