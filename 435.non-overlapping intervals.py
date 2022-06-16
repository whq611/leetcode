class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda x: x[1])
        count = 1
        end = intervals[0][1]
        for i in intervals[1:]:
            if i[0]<end: continue
            count+=1
            end = i[1]
        return len(intervals)-count
