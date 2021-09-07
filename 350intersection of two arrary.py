class Solution:
    def intersect(self, nums1, nums2):
        a = []
        for i in nums1:
            if i in nums2:
                a.append(i)
                nums2.remove(i)
        return a
