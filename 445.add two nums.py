class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        a = ''
        while head1 != None:
            a += str(head1.val)
            head1 = head1.next
        
        a = int(a)

        head2 = l2
        b = ''
        while head2 != None:
            b += str(head2.val)
            head2 = head2.next
        
        b = int(b)
        
        d = []
        c = a + b
        if c == 0:
            return ListNode(0)
        while c != 0:
            f = c % 10
            c = c // 10        
            d.append(f)
        head = ListNode(d[-1])
        cur = head
        for i in d[-2::-1]:
            cur.next = ListNode(i)
            cur = cur.next
        return head
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums1 = [2,4,3]
    nums2 = [5,6,4]
    l1 = create_linked_list(nums1)
    l2 = create_linked_list(nums2)
    solution = Solution()
    result = solution.addTwoNumbers(l1,l2)
    print('结果：')
    print_linked_list(result)
