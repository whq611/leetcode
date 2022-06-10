class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class lj18 {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode prehead = new ListNode(-1,head);
        ListNode cur = prehead;
        while(cur.next!=null && cur.next.val!=val) cur = cur.next;
        cur.next = cur.next.next;
        return prehead.next;
    }
}
