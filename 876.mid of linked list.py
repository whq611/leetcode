class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

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



curr = curr1 = head
l = 1
while curr.next:
    l += 1
    curr = curr.next
l = l // 2
        
while l > 0:
    curr1 = curr1.next
    l -= 1
if not curr1 or not curr1.next:
    print([])
result = []    
while curr1:
    result.append(curr1.val)
    curr1 = curr1.next
print(result)




