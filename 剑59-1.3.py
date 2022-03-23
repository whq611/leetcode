import heapq
class Solution:
    def maxSlidingWindow(self,nums,k):
        if not nums or k <= 0:
            return []
        n = len(nums)
        q = [(-nums[i],i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k,n):
            heapq.heappush(q,(-nums[i].i))
            while q[0][1]<=i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans
            
