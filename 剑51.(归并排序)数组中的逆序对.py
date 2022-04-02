class Solution:
    def reversePairs(self,nums):
        def merge_sort(l,r):
            if l>=r:
                return 0
            m = (l+r)//2
            res = merge_sort(l,m)+merge_sort(m+1,r)
            if nums[m]<=nums[m+1]:
                return res
            i,j = l,m+1
            tmp[l,r+1] = nums[l,r+1]
            for k in range(l,r+1):
                if i == m+1:
                    nums[k] = tmp[j]
                    j+=1
                elif j == r+1 or tmp[i]<=tmp[j]:
                    nums[k] = tmp[i]
                    i+=1
                else:
                    num[k] = tmp[j]
                    j+=1
                    res += m-i+1
            return res



        tmp = [0]*len(nums)
        return merge_sort(0,len(nums)-1)
