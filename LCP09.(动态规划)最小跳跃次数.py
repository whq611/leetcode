class Solution:
    def minJump(self,jump):
        res = n = len(jump)
        f = [n]*(n+1)
        f[0] = 0
        max_dis = [0]*(n+1)
        curr_min_num = 0
        for i in range(0,n):
            if i>=max_dis[curr_min_num]:
                curr_min_num += 1
            f[i] = min(f[i],curr_min_num+1)
            jump_tmp = i+jump[i]
            if jump_tmp>=n:
                res = min(res,f[i]+1)
            else:
                f[jump_tmp] = min(f[jump_tmp],f[i]+1)
                max_dis[f[i]+1] = max(max_dis[f[i]+1],jump_tmp)
        return res
