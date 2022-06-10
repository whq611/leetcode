class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class lj52 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA==null || headB==null) return null;
        ListNode a = headA, b = headB;
        while(a!=null || b!=null){
            if(a==b) return a;
            if(a!=null) a=a.next;
            else a = headB;
            if(b!=null) b = b.next;
            else b = headA;
        }
        return a;
    }
}
