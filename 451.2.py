import heapq
class Solution:
    def frequencySort(self, s):
        counter = {}
        for c in s:
            counter[c] = counter.get(c,0) + 1
        items = [(-val, key) for key, val in counter.items()]
        heapq.heapify(items)
        res = ''
        while items:
            val,key = heapq.heappop(items)
            res += key*(-val)
        return res
