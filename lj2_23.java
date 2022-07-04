class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class lj2_23 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        while(a!=b){
            if(a!=null) a = a.next;
            else a = headB;
            if(b!=null) b = b.next;
            else b = headA;
        }
        return a;
    }
}
