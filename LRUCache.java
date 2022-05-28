import java.util.HashMap;

class ListNode{
    int key;
    int val;
    ListNode next = null;
    ListNode prev = null;
    public ListNode() {}
    public ListNode(int key, int val){
        this.key = key;
        this.val = val;
    }
}

public class LRUCache {
    int capacity;
    HashMap<Integer, ListNode> Sites = new HashMap<Integer, ListNode>();
    ListNode head = new ListNode();
    ListNode tail = new ListNode();


    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public void move_to_tail(int key){
        ListNode node = Sites.get(key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
    }

    public int get(int key) {
        if(Sites.containsKey(key)){
            move_to_tail(key);
            return Sites.get(key).val;
        }
        else return -1;
    }
    
    public void put(int key, int value) {
        if(Sites.containsKey(key)){
            Sites.get(key).val = value;
            move_to_tail(key);
        }
        else{
            if(Sites.size() == capacity){
                Sites.remove(head.next.key);
                head.next = head.next.next;
                head.next.prev = head;
            }
            ListNode node = new ListNode(key,value);
            Sites.put(key,node);
            node.prev = tail.prev;
            node.next = tail;
            tail.prev.next = node;
            tail.prev = node;
            
        }
    }
}
