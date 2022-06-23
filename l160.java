class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class l160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        while(a!=null || b!= null){
            if(a==b) return a;
            if(a.next==null && b.next==null) return null;
            if(a.next!=null) a = a.next;
            else a = headB;
            if(b.next!=null) b = b.next;
            else b = headA;
        }
        return a;
    }
}
