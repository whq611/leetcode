class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class l2_26 {
    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode l2 = slow.next, l1 = head;
        slow.next = null;
        l2 = reverse(l2);
        while(l1!=null && l2!=null){
            ListNode tmp1 = l1.next, tmp2 = l2.next;
            l1.next = l2;
            l2.next = tmp1;
            l1 = tmp1;
            l2 = tmp2;
        }
        
    }
    public ListNode reverse(ListNode head){
        ListNode pre = null;
        while(head!=null){
            ListNode tmp = head.next;
            head.next = pre;
            pre = head;
            head = tmp;
        }
        return pre;
    }
}
