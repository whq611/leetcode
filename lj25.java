class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class lj25 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode prehead = new ListNode();
        ListNode cur = prehead;
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                cur.next = l1;
                l1 = l1.next;
                cur = cur.next;
            }
            else{
                cur.next = l2;
                l2 = l2.next;
                cur = cur.next;
            }
            
        }
        if(l1!=null) cur.next = l1;
        if(l2!=null) cur.next = l2;
        return prehead.next;
    }
}
