class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class lj22 {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode prehead = new ListNode(-1,head);
        ListNode slow = prehead, fast = prehead;
        while(k>0){
            fast = fast.next;
            k--;
        }
        while(fast!=null){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
