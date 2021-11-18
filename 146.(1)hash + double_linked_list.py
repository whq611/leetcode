class ListNode:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None
class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nex = self.tail
        self.tail.pre = self.head
    def move_node_into_tail(self,key):
        self.hashmap[key].pre.nex = self.hashmap[key].nex
        self.hashmap[key].next.pre = self.hashmap[key].pre
        self.hashmap[key].pre = self.tail.pre
        self.hashmap[key].nex = self.tail
        self.tail.pre.nex = self.hashmap[key]
        self.tail.pre = self.hashmap[key]
    def get(self,key):
        if key in self.hashmap:
            self.move_node_into_tail(key)
            return self.hashmap[key].val
        else:
            return -1
    def put(self,key,value):
        if key in self.hashmap:
            self.move_node_into_tail(key)
            self.hashmap[key].val = value
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.nex.key)
                self.head.nex = self.head.nex.nex
                self.head.nex.pre = self.head
            new = ListNode(key,value)
            self.hashmap[key] = new
            self.hashmap[key].pre = self.tail.pre
            self.hashmap[key].nex = self.tail
            self.tail.pre.nex = self.hashmap[key]
            self.tail.pre = self.hashmap[key]
                
