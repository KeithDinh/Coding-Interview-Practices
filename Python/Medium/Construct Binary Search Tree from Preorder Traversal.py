# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        head = TreeNode(preorder.pop(0))
        for i in preorder:
            self.addToTree(head,i)
        
        return head
        
    
    def addToTree(self, current, val):
        if val > current.val:
            if current.right:
                self.addToTree(current.right, val)
            else:
                current.right = TreeNode(val)
        else:
            if current.left:
                self.addToTree(current.left, val)
            else:
                current.left = TreeNode(val)