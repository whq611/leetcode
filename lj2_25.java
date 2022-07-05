class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class lj2_25 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        l1 = reverse(l1);
        l2 = reverse(l2);
        ListNode head = null;
        int carry = 0, val = 0, x = 0, y = 0;
        while(l1!=null || l2!=null || carry!=0){
            x = l1!=null ? l1.val: 0;
            y = l2!=null ? l2.val: 0;
            val = (x+y+carry)%10;
            carry = (x+y+carry)/10;
            ListNode curr = new ListNode(val);
            curr.next = head;
            head = curr;
            if(l1!=null) l1 = l1.next;
            if(l2!=null) l2 = l2.next;
        }
        return head;
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
