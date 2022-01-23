import heapq
class Solution:
    def getLeastNumbers(self,arr,k):
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(l,len(arr)):
            if -hp[0]>arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp,-arr[i])
        ans = [-x for x in hp]
        return ans
