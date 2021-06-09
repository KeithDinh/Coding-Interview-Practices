# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        arr = []
        self.sumByLevel(root, 0, arr)
        return arr[-1]
        
    
    def sumByLevel(self, current, n, arr):
        if not current:
            return
        if n < len(arr):
            arr[n] = arr[n] + current.val
        else:
            arr.append(current.val)
        
        self.sumByLevel(current.left, n+1, arr)
        self.sumByLevel(current.right, n+1, arr)