class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
                continue
            ans.append(intervals[i])
        ans.append(intervals[-1])
        return ans
