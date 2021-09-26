class Solution:
    def findClosestElements(self, arr, k, x):
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            mid = left + (right - left)//2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]
