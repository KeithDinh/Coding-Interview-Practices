# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if not lists:
            return None
        
        length = len(lists)
        
        startList = lists[0]
        
        for i in range(1, length):
            startList = self.merge2Lists(startList, lists[i])
        
        return startList
    
    def merge2Lists(self, start, current):
        if not start:
            return current
        elif not current:
            return start
        
        head = ListNode()
        temp = head
        
        while start != None and current != None:
            if start.val >= current.val:
                temp.next = current
                current = current.next
            else:
                temp.next = start
                start = start.next
            temp = temp.next
        
        if not current:
            temp.next = start
        else:
            temp.next = current
            
        return head.next