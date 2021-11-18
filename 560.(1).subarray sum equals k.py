class Solution:
    def subarraySum(self,nums,k):
        result = 0
        sums = 0
        hashmap = {}
        hashmap[0] = 1

        for i in nums:
            sums += i
            if sums-k in hashmap:
                result += hashmap[sums-k]
            hashmap[sums] = hashmap.get(sums,0) + 1
        return result
