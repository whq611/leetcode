class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2 

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
    nums1 = [1,2,4]
    nums2 = [1,3,4]
    l1 = create_linked_list(nums1)
    l2 = create_linked_list(nums2)
    solution = Solution()
    result = solution.mergeTwoLists(l1,l2)
    print('结果：')
    print_linked_list(result)
