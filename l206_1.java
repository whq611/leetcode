class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class l206_1 {
    public ListNode reverseList(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode pre = head;
        ListNode cur = head.next;
        pre.next = null;
        while(cur!=null){
            ListNode tmp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
}
