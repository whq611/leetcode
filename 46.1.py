class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path,used):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(path,used)
                    path.pop()
                    used[i] = False
        
        res = []
        if not nums:
            return res
        path = []
        used = [False] * len(nums)
        dfs(path,used)
        return res
