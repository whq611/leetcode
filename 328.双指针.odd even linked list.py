class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        l1 = head
        l2 = head.next
        while l2.next and l2.next.next:            
            c = l1.next
            d = l2.next.next
            l1.next = l2.next
            l2.next.next = c
            l2.next = d
            l1 = l1.next
            l2 = l2.next
        if l2.next:                
            l2.next.next = l1.next
            l1.next = l2.next
            l2.next = None
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
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.oddEvenList(head)
    print('结果：')
    print_linked_list(result)
