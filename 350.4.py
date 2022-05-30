class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        for i in nums1:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        res = []
        for i in nums2:
            if i in a and a[i] != 0:
                a[i] -= 1
                res.append(i)
        return res
