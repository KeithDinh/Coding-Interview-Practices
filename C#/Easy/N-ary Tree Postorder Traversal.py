"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        queue = [root]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.insert(0, current.val)
            queue = [i for i in reversed(current.children)] + queue
        
        return result