class Solution:
    def exclusiveTime(self,n,logs):
        res = [0] * n
        stack = []
        pre = 0
        for s in logs:
            cur = s.split(':')
            if cur[1] == 'start':
                if stack:
                    res[stack[-1]] += int(cur[2]) - pre
                stack.append(int(cur[0]))
            else:
                res[stack.pop()] += int(cur[2]) - pre + 1
                pre = int(cur[2]) + 1
        return res
