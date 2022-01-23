class Solution:
    def minNumber(self, nums):
        def quick_sort(l,r):
            if l>=r:
                return
            i,j = l,r
            while i<j:
                while strs[j]+strs[l]>=strs[l]+str[j] and i<j:
                    j -= 1
                while strs[i]+strs[l]<=strs[l]+strs[i] and i<j:
                    i += 1
                strs[i],strs[j] = strs[j],strs[i]
            strs[i],strs[l] = strs[l],strs[i]
            quilk_sort(l,i-1)
            quilk_sort(i+1,r)
        strs = [str(num) for num in nums]
        quick_sort(0,len(strs)-1)
        return ''.join(strs)
            
