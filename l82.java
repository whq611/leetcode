class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class l82 {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head, pre = new ListNode(-101,head), a = pre;
        while(cur!=null){
            if(cur.next==null || cur.next.val != cur.val){
                pre.next = cur;
                pre = cur;
            }
            while(cur.next!=null && cur.next.val==cur.val){
                cur.next = cur.next.next;
            }
            cur = cur.next;
            
        }
        pre.next = null;

        return a.next;
    }
}
