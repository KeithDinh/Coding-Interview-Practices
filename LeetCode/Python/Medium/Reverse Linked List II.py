# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        cur = head
        prev = None
        
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        
        connection = prev
        tail = cur
        
        while n > 0:
            nextone = cur.next
            cur.next = prev
            prev = cur
            cur = nextone
            n -= 1
        
        if connection is not None:
            connection.next = prev
        else:
            head = prev
            
        tail.next = cur
        return head