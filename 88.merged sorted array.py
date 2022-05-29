class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = len(nums1)-m
        while a>0:
            nums1.pop()
            a-=1
        nums2 = nums2[:n]
        nums1.extend(nums2)
        nums1.sort()
