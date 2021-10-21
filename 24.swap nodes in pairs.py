class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            c = head.next
        a = head
        while a != None and a.next != None and a.next.next != None and a.next.next.next != None:
            b = a.next.next
            a.next.next = a
            a.next = b.next
            a = b       
        else:

            while a != None and a.next != None:
                b = a.next.next
                a.next.next = a
                a.next = b
                a = b
        return c


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
    result = solution.swapPairs(head)
    print('结果：')
    print_linked_list(result)
