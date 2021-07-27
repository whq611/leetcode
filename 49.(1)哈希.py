import collections
class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())
            
            
