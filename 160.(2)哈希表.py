class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        s = set()
        p, q = headA, headB
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            q = q.next
        return None



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
    nums1 = [4, 1, 8, 4, 5]
    nums2 = [5, 6, 1, 8, 4, 5]
    head1 = create_linked_list(nums1)
    head2 = create_linked_list(nums2)
    head1.next.next = head2.next.next.next
    solution = Solution()
    result = solution.getIntersectionNode(head1, head2)
    print('结果：')
    print_linked_list(result)
