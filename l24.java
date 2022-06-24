class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class l24 {
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode prehead = new ListNode(-1,head);
        ListNode pre = prehead, cur = head;
        while(cur!=null && cur.next!=null){
            pre.next = cur.next;
            ListNode tmp = cur.next.next;
            cur.next.next = cur;
            cur.next = tmp;
            pre = pre.next.next;
            cur = cur.next;
        }
        return prehead.next;
    }
}
