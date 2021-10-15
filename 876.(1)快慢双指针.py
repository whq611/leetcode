class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
node1 = Node(3)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1
print(middleNode(head).val)
