class Solution:
    def countSmaller(self,nums):
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        
        temp = [None for _ in range(size)]
        res = [0 for _ in range(size)]
        indexes = [i for i in range(size)]

        self._merge_and_count_smaller(nums,0,size-1,temp,indexes,res)
        return res

    def _merge_and_count_smaller(self,nums,left,right,temp,indexes,res):
        if left == right:
            return
        mid = left + (right - left) // 2
        self._merge_and_count_smaller(nums,left,mid,temp,indexes,res)
        self._merge_and_count_smaller(nums,mid+1,right,temp,indexes,res)

        if nums[indexes[mid]] <= nums[indexes[mid+1]]:
            return
        self._sort_and_count_smaller(nums,left,mid,right,temp,indexes,res)

    def _sort_and_count_smaller(self,nums,left,mid,right,temp,indexes,res):
        for i in range(left,right+1):
            temp[i] = indexes[i]
        i = left
        j = mid + 1
        for k in range(left,right+1):
            if i > mid:
                indexes[k] = temp[j]
                j += 1
            elif j > right:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (right - mid)
            elif nums[temp[i]] <= nums[temp[j]]:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (j - mid - 1)
            else:
                indexes[k] = temp[j]
                j += 1
