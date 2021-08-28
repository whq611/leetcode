class Solution:
    def intersection(self,nums1,nums2):
        nums1.sort()
        nums2.sort()
        l1,l2 = len(nums1),len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < l1 and index2 < l2:
            num1 = nums1[index1]
            num2 = nums2[index2]
            if num1 == num2:
                if not intersection or num1 != intersection[-1]:
                    intersection.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1
        return intersection
