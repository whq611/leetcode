import collections
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)

        m = collections.Counter(nums1)
        intersection = list()
        for num in nums2:
            if (count := m[num]) > 0:
                intersection.append(num)
                m[num] -= 1

        return intersection
        
        
