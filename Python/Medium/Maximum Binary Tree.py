# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        currentMax = max(nums)
        pos = nums.index(currentMax)
        
        root = TreeNode(currentMax)
        
        root.left = self.constructMaximumBinaryTree(nums[0:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos+1:])
        
        return root