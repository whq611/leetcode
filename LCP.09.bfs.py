class Solution:
    def minJump(self,jump):
        visit = [0 for _ in range(len(jump))]
        q = [(0,0)]
        visit[0] = 1
        max_left_dix = 0
        while q:
            cur_idx,count = q.pop(0)
            right_idx = cur_idx + jum[cur_idx]
            if right_idx >= len(jump):
                return count + 1
            else:
                if not visit[right_idx]:
                    q.append((right_idx,count+1))
                    visit[right_idx] = 1
            for i in range(max_left_idx+1,cur_idx):
                if not visit[i]:
                    q.append((i,count + 1))
                    visit[i] = 1
            max_left_idx = max(cur_idx,max_left_idx)
