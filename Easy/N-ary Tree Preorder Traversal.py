"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        deq = [root]
        result = []
        while deq:
            current = deq.pop(0)
            result.append(current.val)
            deq = [i for i in current.children] + deq
            
        return result