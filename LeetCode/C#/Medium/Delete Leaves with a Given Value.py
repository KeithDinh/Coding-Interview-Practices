# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root: TreeNode) -> bool:
            return True if root.right is None and root.left is None else False
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        elif root.val == target and self.isLeaf(root):
            return None
        else:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            
            if root.val == target and self.isLeaf(root):
                return None
            else:
                return root
    