class Solution:
    def topKFrequent(self,nums,k):
        hashmap = dict()
        buckets = [[] for _ in range(len(nums)+1)]
        for i,val in enumerate(nums):
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for num,freq in hashmap.items():
            buckets[freq].append(nums)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                if len(res) == k:
                    return res
