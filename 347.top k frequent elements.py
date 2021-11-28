class Solution:
    def topKFrequent(self, nums, k):
        hashmap = dict()
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        
        a = sorted(hashmap.items(),key = lambda x:x[1],reverse = True)
        res = []
        b = 0
        for i,val in a:
            if b<k:
                res.append(i)
                b += 1
            else:
                break
        return res
