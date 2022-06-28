class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class l234 {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode a = slow.next;
        while(a!=null){
            ListNode tmp = a.next;
            a.next = slow;
            slow = a;
            a = tmp;
        }
        while(head.next!=slow && head.next!=slow.next){
            if(head.val!=slow.val) return false;
            head = head.next;
            slow = slow.next;
        }
        if(head.val!=slow.val) return false;
        return true;
    }
}
