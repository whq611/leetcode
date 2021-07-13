class Solution:
    def increasingTriplet(self, nums):
        a = sorted(set(nums))
        for i in range(len(a)-2):
            for j in range(i+1,len(a)-1):
                try:
                    if nums.index(a[i]) < nums.index(a[j],nums.index(a[i])+1):
                        for k in range(j+1,len(a)):
                            try:
                                if nums.index(a[j],nums.index(a[i])+1) < nums.index(a[k],nums.index(a[j],nums.index(a[i])+1)+1):
                                    return True
                            except (ValueError):
                                continue
                except (ValueError):
                    continue
        return False
