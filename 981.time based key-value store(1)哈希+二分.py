from collections import defaultdict
from bisect import bisect_right
class TimeMap:
    def __init__(self):
        self.dct = defaultdict(list)

    def set(self,key,value,timestamp):
        self.dct[key].append([timestamp,value])

    def get(self,key,timestamp):
        a = bisect_right(self.dct[key],[timestamp,'z'*101])
        if a == 0:
            return ''
        return (self.dct[key])[a-1][1]
        
