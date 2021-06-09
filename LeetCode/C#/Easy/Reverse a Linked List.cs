public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return head;
        }
        if(head.next == null)
            return head;
        ListNode cur = ReverseList(head.next);
        
        head.next.next = head;
        head.next = null;
        
        return cur;
    }
}