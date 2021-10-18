class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        cur3 = head = ListNode(0)
        while cur1 or cur2:        
            if not cur1:
                cur3.next = cur2
                cur2 = cur2.next
                cur3 = cur3.next
            elif not cur2:
                cur3.next = cur1
                cur1 = cur1.next
                cur3 = cur3.next
            elif cur1.val>=cur2.val:
                cur3.next = cur2
                cur2 = cur2.next
                cur3 = cur3.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
                cur3 = cur3.next
        return head.next

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
