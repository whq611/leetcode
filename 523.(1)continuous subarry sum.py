class Solution:
    def checkSubarraySum(self,nums,k):
        dic = {0:-1}
        presum = 0
        for i,n in enumerate(nums):
            if k!=0:
                presum = (presum+n)%k
            else:
                presum += n
            if presum in dic:
                if i - dic[presum] >= 2:
                    return True
            else:
                dic[presum] = i
        return False 
