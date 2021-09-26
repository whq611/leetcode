class Solution:
    def findClosestElements(self, arr, k, x):
        size = len(arr)
        left = 0
        right = size - 1

        remove_nums = size - k
        while remove_nums:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1

            remove_nums -= 1

        return arr[left:left+k]
