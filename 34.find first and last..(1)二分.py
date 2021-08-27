class Solution:
    def searchRange(self,nums,target):
        if len(nums) == 0:
            return [-1,-1]
        res = []
        def left_bound(nums,target):
            l,r = 0,len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if l > len(nums) - 1 or nums[l] != target:
                res.append(-1)
            else:
                res.append(l)

        def right_bound(nums,target):
            l,r = 0,len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if r < 0 or nums[r] != target:
                res.append(-1)
            else:
                res.append(r)

        left_bound(nums,target)
        right_bound(nums,target)
        return res
                
                
