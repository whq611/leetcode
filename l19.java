class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class l19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode prehead = new ListNode(-1,head);
        ListNode slow = prehead, fast = prehead;
        while(n>0){
            fast = fast.next;
            n--;
        }
        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return prehead.next;
    }
}
