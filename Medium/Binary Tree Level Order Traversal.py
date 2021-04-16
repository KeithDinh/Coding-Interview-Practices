# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        else:
            levelDict = {}
            self.storeLevel(root, levelDict, 0)
            return [levelDict[i] for i in levelDict.keys()]
        
    
    def storeLevel(self, current, d, level):
        if current is None:
            return
        else:
            if level in d:
                d[level].append(current.val)
            else:
                d[level] = [current.val]
            self.storeLevel(current.left, d, level+1)
            self.storeLevel(current.right, d, level+1)